from requests import Session, get
from bs4 import BeautifulSoup
from pprint import pprint


def get_token(app_id, scopes_argument, login, password):
    # Если нам дали список
    if type(scopes_argument) is list:
        # То соединяем список
        scopes = ','.join(scopes_argument)
    else:
        # Иначе просто говорим что переменная scopes это scopes из аргументов
        scopes = scopes_argument
    # Начинаем новую сессию
    # -------------------
    # Сессия это механизм, который позволяет отследить запросы от одного браузера
    # и сохранить некоторые переменные во время переходов по страницам сайта.
    # https://training.qatestlab.com/blog/technical-articles/cookies-cache-session-in-browser/
    # -------------------
    with Session() as session:
        # Заходим на страницу авторизации
        rq = session.get(
            f"https://oauth.vk.com/authorize?client_id={app_id}&redirect_uri=http://vk.com&scope={scopes}"
            "&display=mobile&response_type=token&v=5.130"
        )
        login_page_soap = BeautifulSoup(rq.content, "lxml")
        inputs = login_page_soap.find_all("input")
        # Авторизируемся
        rq_auth = session.post(
            "https://login.vk.com/?act=login&soft=1&utf8=1", {
                "origin": "https://oauth.vk.com",
                "ip_h": inputs[1]['value'],
                "lg_h": inputs[2]['value'],
                "to": inputs[3]['value'],
                "email": login,
                "pass": password
            })
        # Смотрим какая страница
        symbool = rq_auth.url.find("#")
        # Если нам дали страницу с потверждением прав доступа
        if symbool == -1:
            # То берём из формы ссылку на потверждение прав доступа
            access_page_soap = BeautifulSoup(rq_auth.content, "lxml")
            form = access_page_soap.find("form")
            url = form['action']
            access_rq = session.get(url)
            split_url = access_rq.url.split("#")
        else:
            # Если мы уже на странице с токеном то делим url на url и параметры
            split_url = rq_auth.url.split("#")
    # Разделяем параметры
    parameters = split_url[1].split("&")
    # Берём access token
    access_token = parameters[0].split("=")
    # И user_id
    user_id = parameters[2].split("=")
    return access_token, user_id


class VkApi:
    def __init__(self, token):
        self.token = token

    def send_request(self, method, fields_json, debug=False):
        # Превращаем json в список
        fields = fields_json.items()
        # Превращаем все элементы списка в str
        str_fields = []
        for str_field in fields:
            str_fields.append((str(str_field[0]), str(str_field[1])))
        # Соединяем элементы
        pre_url_fields = []
        for field in str_fields:
            pre_url_fields.append("=".join(field))
        url_fields = "&".join(pre_url_fields)
        # Отсылаем запрос к api vk
        url = f"https://api.vk.com/method/{method}?{url_fields}&access_token={self.token}&v=5.130"
        if debug is True:
            print(url)
            print(url_fields)
        rq = get(url)
        # Возращаем ответ приведённый в json
        return rq.json()


class Friends(VkApi):
    """
    Класс для работы с друзьями
    """

    def get_friends(self, order="name", fields="nickname", count=5000):
        """
        Возвращает список идентификаторов друзей пользователя
        или расширенную информацию о друзьях пользователя (при использовании параметра fields).
        """
        friends = self.send_request("friends.get", {
            "order": order,
            "fields": fields,
            "count": count
        })
        return friends

    def get_recent(self, count=100):
        """
        Возращает список идентификаторов  недавно добавленных друзей текущего пользователя.
        """
        recent_friends = self.send_request("friends.getRecent", {
            "count": count
        })
        return recent_friends

    def get_online(self, list_id="", online_mobile=0, order="", count=5000):
        """
        Возвращает список идентификаторов друзей пользователя, находящихся на сайте
        """
        online_friends = self.send_request(
            "friends.getOnline", {
                "list_id": list_id,
                "online_mobile": online_mobile,
                "order": order,
                "count": count
            })
        return online_friends

    def search(self, query, fields="", name_case="Nom", count=20):
        """
        Метод позволяет искать по списку друзей пользователей
        """
        search_friends = self.send_request(
            "friends.search", {
                "q": query,
                "fields": fields,
                "name_case": name_case,
                "count": count
            })
        return search_friends

    def are_friends(self, user_ids, extended=0):
        """
        Возвращает информацию о том, добавлен ли текущий пользователь в друзья у указанных пользователей.
        """
        are_friends = self.send_request(
            "friends.areFriends", {
                "user_ids": user_ids,
                "extended": extended
            })
        return are_friends

    def delete(self, user_id):
        """
        Удаляет пользователя из списка друзей или отклоняет заявку в друзья
        """
        delete_friend = self.send_request(
            "friends.delete", {
                "user_id": user_id
            }
        )
        return delete_friend

    def delete_all_requests(self):
        """
        Отмечает все входящие заявки на добавление в друзья как просмотренные.
        """
        delete_all_requests = self.send_request(
            "friends.deleteAllRequests", {}
        )
        return delete_all_requests

    def add(self, user_id, follow, text=""):
        """
        Одобряет или создает заявку на добавление в друзья.
        """
        add_friends = self.send_request(
            "friends.add", {
                "user_id": user_id,
                "text": text,
                "follow": follow
            })
        return add_friends

    def add_list(self, name, user_ids=""):
        """
        Создает новый список друзей у текущего пользователя.
        """
        add_list = self.send_request(
            "friends.addList", {
                "name": name,
                "user_ids": user_ids,
            })
        return add_list

    def get_lists(self, user_id="", return_system=0):
        """
        Возвращает список меток друзей пользователя.
        """
        list_friends = self.send_request(
            "friends.getLists", {
                "user_id": user_id,
                "return_system": return_system
            })
        return list_friends

    def get_requests(self, count=100, extended=0, need_mutual=0, out=0, sort=0):
        """
        Возвращает информацию о полученных или отправленных заявках на добавление в друзья для текущего пользователя.
        """
        get_requests = self.send_request(
            "friends.getRequests", {
                "count": count,
                "extended": extended,
                "need_mutual": need_mutual,
                "out": out,
                "sort": sort
            })
        return get_requests

    def delete_list(self, list_id):
        """
        Удаляет существующий список друзей текущего пользователя.
        """
        delete_list = self.send_request(
            "friends.deleteList", {
                "list_id": list_id
            })
        return delete_list

    def edit(self, user_id, list_ids):
        """
        Редактирует списки друзей для выбранного друга.
        """
        edit_friends = self.send_request(
            "friends.edit", {
                "user_id": str(user_id),
                "list_ids": str(list_ids)
            })
        return edit_friends

    def get_suggestions(self, filter_friends="", count=500, fields="", name_case="nom"):
        """
        Возвращает список профилей пользователей, которые могут быть друзьями текущего пользователя.
        """
        get_suggestions = self.send_request(
            "friends.getSuggestions", {
                "filter": filter_friends,
                "count": count,
                "fields": fields,
                "name_case": name_case
            })
        return get_suggestions

    def get_app_users(self):
        """
        Возвращает список идентификаторов друзей текущего пользователя, которые установили данное приложение.
        """
        get_app_users = self.send_request(
            "friends.getAppUsers", {}
        )
        return get_app_users

    def get_by_phones(self, phones, fields=""):
        """
        Возвращает список друзей пользователя,
        у которых завалидированные или указанные в профиле телефонные номера входят в заданный список.
        """
        get_by_phones = self.send_request(
            "friends.getByPhones", {
                "phones": phones,
                "fields": fields
            })
        return get_by_phones


class Status(VkApi):
    """
    Класс для работы со статусом
    """

    def get(self, user_id="", group_id=""):
        """
        Получает текст статуса пользователя или сообщества.
        """
        status = self.send_request(
            "status.get", {
                "user_id": user_id,
                "group_id": group_id
            })
        return status

    def set(self, text, group_id=""):
        """
        Устанавливает новый статус текущему пользователю или сообществу.
        """
        new_status = self.send_request(
            "status.set", {
                "text": text,
                "group_id": group_id
            })
        return new_status


class Notifications(VkApi):
    """
    Класс для работы с уведомлениями
    """

    def get(self, **kwargs):
        """
        Возвращает список оповещений об ответах других пользователей на записи текущего пользователя.
        """
        notifications = self.send_request(
            "notifications.get", kwargs
        )
        return notifications

    def mark_as_viewed(self):
        """
        Сбрасывает счетчик непросмотренных оповещений
        об ответах других пользователей на записи текущего пользователя.
        """
        reset_notifications = self.send_request(
            "notifications.markAsViewed", {}
        )
        return reset_notifications


class Account(VkApi):
    """
    Класс для работы с аккаунтом
    """

    def set_offline(self):
        """
        Помечает текущего пользователя как offline (только в текущем приложении).
        """
        set_offline = self.send_request(
            "account.setOffline", {}
        )
        return set_offline

    def get_info(self, fields=""):
        """
        Возвращает информацию о текущем аккаунте.
        """
        info = self.send_request(
            "account.getInfo", {
                "fields": fields
            })
        return info

    def get_profile_info(self):
        """
        Возвращает информацию о текущем профиле.
        """
        profile_info = self.send_request(
            "account.getProfileInfo", {}
        )
        return profile_info

    def get_counters(self, filter_counters=""):
        """
        Возвращает ненулевые значения счетчиков пользователя.
        """
        counters = self.send_request(
            "account.getCounters", {
                "filter": filter_counters
            })
        return counters

    def get_banned(self, count=20):
        """
        Возвращает список пользователей, находящихся в черном списке.
        """
        users_banned = self.send_request(
            "account.getBanned", {
                "count": count
            })
        return users_banned

    def get_app_permissions(self, user_id=""):
        """
        Получает настройки текущего пользователя в данном приложении.
        """
        app_permissions = self.send_request(
            "account.getAppPermissions", {
                "user_id": user_id
            })
        return app_permissions

    def get_active_offers(self, count=100):
        """
        Возвращает список активных рекламных предложений
        """
        active_offers = self.send_request(
            "account.getActiveOffers", {
                "count": count
            })
        return active_offers

    def get_push_settings(self, device_id=""):
        """
        Позволяет получать настройки Push-уведомлений.
        """
        push_settings = self.send_request(
            "account.getPushSettings", {
                "device_id": device_id
            })
        return push_settings

    def ban(self, owner_id):
        """
        Добавляет пользователя или группу в черный список.
        """
        ban = self.send_request(
            "account.ban", {
                "owner_id": owner_id
            })
        return ban

    def unban(self, owner_id):
        """
        Удаляет пользователя или группу из черного списка.
        """
        unban = self.send_request(
            "account.unban", {
                "owner_id": owner_id
            })
        return unban

    def set_online(self, voip=""):
        """
        Помечает текущего пользователя как online на 5 минут.
        """
        set_online = self.send_request(
            "account.setOnline", {
                "voip": voip
            })
        return set_online

    def set_name_in_menu(self, name, user_id=""):
        """
        Устанавливает короткое название приложения
        """
        name_in_menu = self.send_request(
            "account.setNameInMenu", {
                "user_id": user_id,
                "name": name
            })
        return name_in_menu

    def set_info(self, **kwargs):
        """
        Позволяет редактировать информацию о текущем аккаунте.
        """
        info = self.send_request(
            "account.setInfo", kwargs
        )
        return info

    def save_profile_info(self, **kwargs):
        """
        Редактирует информацию текущего профиля.
        """
        profile_info = self.send_request(
            "account.saveProfileInfo", kwargs
        )
        return profile_info


class Wall(VkApi):
    """
    Класс для работы со стеной
    """

    def get(self, **kwargs):
        """
        Возвращает список записей со стены пользователя или сообщества.
        """
        wall = self.send_request(
            "wall.get", kwargs
        )
        return wall

    def post(self, **kwargs):
        """
        Позволяет создать запись на стене,
        предложить запись на стене публичной страницы,
        опубликовать существующую отложенную запись.
        """
        post = self.send_request(
            "wall.post", kwargs
        )
        return post

    def delete(self, **kwargs):
        """
        Удаляет запись со стены.
        """
        delete_post = self.send_request(
            "wall.delete", kwargs
        )
        return delete_post

    def pin(self, **kwargs):
        """
        Закрепляет запись на стене
        """
        pin_post = self.send_request(
            "wall.pin", kwargs
        )
        return pin_post

    def unpin(self, **kwargs):
        """
        Отменяет закрепление записи на стене.
        """
        unpin_post = self.send_request(
            "wall.unpin", kwargs
        )
        return unpin_post

    def get_comments(self, **kwargs):
        """
        Возвращает список комментариев к записи на стене.
        """
        comments = self.send_request(
            "wall.getComments", kwargs
        )
        return comments

    def get_comment(self, **kwargs):
        """
        Получает информацию о комментарии на стене.
        """
        comment = self.send_request(
            "wall.getComment", kwargs
        )
        return comment

    def open_comments(self, owner_id, post_id):
        """
        Включает комментирование записи
        Работает только с конкретными записями,
        комментирование которых было выключено с помощью close_comments
        """
        open_comments = self.send_request(
            "wall.openComments", {
                "owner_id": owner_id,
                "post_id": post_id
            })
        return open_comments

    def close_comments(self, owner_id, post_id):
        """
        Выключает комментирование записи
        """
        close_comments = self.send_request(
            "wall.closeComments", {
                "owner_id": owner_id,
                "post_id": post_id
            })
        return close_comments

    def restore(self, owner_id, post_id):
        """
        Восстанавливает удаленную запись на стене пользователя или сообщества.
        """
        restore_post = self.send_request(
            "wall.restore", {
                "owner_id": owner_id,
                "post_id": post_id
            })
        return restore_post

    def repost(self, **kwargs):
        """
        Копирует объект на стену пользователя или сообщества.
        """
        repost = self.send_request(
            "wall.repost", kwargs
        )
        return repost

    def delete_comment(self, **kwargs):
        """
        Удаляет комментарий к записи на стене.
        """
        delete_comment = self.send_request(
            "wall.deleteComment", kwargs
        )
        return delete_comment

    def create_comment(self, **kwargs):
        """
        Добавляет комментарий к записи на стене.
        """
        create_comment = self.send_request(
            "wall.createComment", kwargs
        )
        return create_comment

    def search(self, **kwargs):
        """
        Позволяет искать записи на стене в соответствии с заданными критериями.
        """
        search = self.send_request(
            "wall.search", kwargs
        )
        return search

    # def delete_comment(self, comment_id, owner_id=""):


token = get_token(7779574, "wall,status", "+37362159808", "andrei2006telus")
print(token)