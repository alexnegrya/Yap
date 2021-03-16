from json import dump, load
from bs4 import BeautifulSoup
from requests import get, Session


def get_current_version():
    rq = get("https://vk.com/dev/versions")
    soap = BeautifulSoup(rq.content, "lxml")
    version_html = soap.find(class_="dev_version_num")
    return version_html.string


def get_all_versions():
    rq = get("https://vk.com/dev/versions")
    soap = BeautifulSoup(rq.content, "lxml")
    versions_html = soap.find_all(class_="dev_version_num")
    versions = []
    for version in versions_html:
        versions.append(version.string)
    return versions


class Authorize:
    def __init__(self, app_id, rights_argument, redirect_uri, login, password, save_arguments=False):
        self.app_id = app_id
        self.redirect_uri = redirect_uri
        self.login = login
        self.password = password
        if save_arguments is True:
            user_config = {
                "app_id": app_id,
                "rights": rights_argument,
                "redirect_uri": redirect_uri,
                "login": login,
                "password": password
            }
            file = open("user_config.json", "w", encoding="utf-8")
            dump(user_config, file, indent=4)
            file.close()
        # Если нам дали список
        if type(rights_argument) is list:
            # То соединяем список
            self.rights = ','.join(rights_argument)
        else:
            # Иначе просто говорим что переменная rights это rights из аргументов
            self.rights = rights_argument

    def group(self, response_type, group_ids):
        """
        Метод для получения ключа доступа группы
        """
        with Session() as session:
            # Заходим на страницу авторизации
            rq = session.get(
                f"https://oauth.vk.com/authorize?client_id={self.app_id}"
                f"&redirect_uri={self.redirect_uri}&scope={self.rights}"
                f"&group_ids={group_ids}&display=mobile&response_type={response_type}&v={get_current_version()}"
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
                    "email": self.login,
                    "pass": self.password
                })
            # Если сказали дать токен
            if response_type == "token":
                # То начинаем получать токен
                # Смотрим какая страница
                symbool = rq_auth.url.find("token=")
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
                access_token = parameters[1].split("=")
                return access_token[1]
            else:
                # Если сказали дать код начинаем получения кода
                access_page_soap = BeautifulSoup(rq_auth.content, "lxml")
                form = access_page_soap.find("form")
                url = form['action']
                access_rq = session.get(url)
                split_url = access_rq.url.split("=")
                return split_url[1]

    def user(self, response_type):
        """
        Метод для получения ключа доступа пользователя
        """
        # Начинаем новую сессию
        # -------------------
        # Сессия это механизм, который позволяет отследить запросы от одного браузера
        # и сохранить некоторые переменные во время переходов по страницам сайта.
        # https://training.qatestlab.com/blog/technical-articles/cookies-cache-session-in-browser/
        # -------------------
        with Session() as session:
            # Заходим на страницу авторизации
            rq = session.get(
                f"https://oauth.vk.com/authorize?client_id={self.app_id}"
                f"&redirect_uri={self.redirect_uri}&scope={self.rights}"
                f"&display=mobile&response_type={response_type}&v={get_current_version()}"
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
                    "email": self.login,
                    "pass": self.password
                })
            # Если сказали дать токен
            if response_type == "token":
                # Смотрим какая страница
                symbool = rq_auth.url.find("token=")
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
                return access_token[1], user_id[1]
            else:
                # Если сказали дать код начинаем получения кода
                access_page_soap = BeautifulSoup(rq_auth.content, "lxml")
                form = access_page_soap.find("form")
                url = form['action']
                access_rq = session.get(url)
                split_url = access_rq.url.split("=")
                return split_url[1]


def authorization_by_config(response_type, path="user_config.json"):
    json_file = open(path, "r")
    json = load(json_file)
    json_file.close()
    user_config = list(json.values())
    authorize = Authorize(user_config[0], user_config[1], user_config[2], user_config[3], user_config[4])
    return authorize.user(response_type)
