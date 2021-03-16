from requests import get


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


class Account(VkApi):
    def ban(self, **kwargs):
        ban = self.send_request(
            "account.ban", kwargs
        )
        return ban

    def change_password(self, **kwargs):
        change_password = self.send_request(
            "account.changePassword", kwargs
        )
        return change_password

    def get_active_offers(self, **kwargs):
        get_active_offers = self.send_request(
            "account.getActiveOffers", kwargs
        )
        return get_active_offers

    def get_app_permissions(self, **kwargs):
        get_app_permissions = self.send_request(
            "account.getAppPermissions", kwargs
        )
        return get_app_permissions

    def get_banned(self, **kwargs):
        get_banned = self.send_request(
            "account.getBanned", kwargs
        )
        return get_banned

    def get_counters(self, **kwargs):
        get_counters = self.send_request(
            "account.getCounters", kwargs
        )
        return get_counters

    def get_info(self, **kwargs):
        get_info = self.send_request(
            "account.getInfo", kwargs
        )
        return get_info

    def get_profile_info(self, **kwargs):
        get_profile_info = self.send_request(
            "account.getProfileInfo", kwargs
        )
        return get_profile_info

    def get_push_settings(self, **kwargs):
        get_push_settings = self.send_request(
            "account.getPushSettings", kwargs
        )
        return get_push_settings

    def register_device(self, **kwargs):
        register_device = self.send_request(
            "account.registerDevice", kwargs
        )
        return register_device

    def save_profile_info(self, **kwargs):
        save_profile_info = self.send_request(
            "account.saveProfileInfo", kwargs
        )
        return save_profile_info

    def set_info(self, **kwargs):
        set_info = self.send_request(
            "account.setInfo", kwargs
        )
        return set_info

    def set_name_in_menu(self, **kwargs):
        set_name_in_menu = self.send_request(
            "account.setNameInMenu", kwargs
        )
        return set_name_in_menu

    def set_offline(self, **kwargs):
        set_offline = self.send_request(
            "account.setOffline", kwargs
        )
        return set_offline

    def set_online(self, **kwargs):
        set_online = self.send_request(
            "account.setOnline", kwargs
        )
        return set_online

    def set_push_settings(self, **kwargs):
        set_push_settings = self.send_request(
            "account.setPushSettings", kwargs
        )
        return set_push_settings

    def set_silence_mode(self, **kwargs):
        set_silence_mode = self.send_request(
            "account.setSilenceMode", kwargs
        )
        return set_silence_mode

    def unban(self, **kwargs):
        unban = self.send_request(
            "account.unban", kwargs
        )
        return unban

    def unregister_device(self, **kwargs):
        unregister_device = self.send_request(
            "account.unregisterDevice", kwargs
        )
        return unregister_device


class Ads(VkApi):
    def add_office_users(self, **kwargs):
        add_office_users = self.send_request(
            "ads.addOfficeUsers", kwargs
        )
        return add_office_users

    def check_link(self, **kwargs):
        check_link = self.send_request(
            "ads.checkLink", kwargs
        )
        return check_link

    def create_ads(self, **kwargs):
        create_ads = self.send_request(
            "ads.createAds", kwargs
        )
        return create_ads

    def create_campaigns(self, **kwargs):
        create_campaigns = self.send_request(
            "ads.createCampaigns", kwargs
        )
        return create_campaigns

    def create_clients(self, **kwargs):
        create_clients = self.send_request(
            "ads.createClients", kwargs
        )
        return create_clients

    def create_look_a_like_request(self, **kwargs):
        create_look_a_like_request = self.send_request(
            "ads.createLookalikeRequest", kwargs
        )
        return create_look_a_like_request

    def create_target_group(self, **kwargs):
        create_target_group = self.send_request(
            "ads.createTargetGroup", kwargs
        )
        return create_target_group

    def create_target_pixel(self, **kwargs):
        create_target_pixel = self.send_request(
            "ads.createTargetPixel", kwargs
        )
        return create_target_pixel

    def delete_ads(self, **kwargs):
        delete_ads = self.send_request(
            "ads.deleteAds", kwargs
        )
        return delete_ads

    def delete_campaigns(self, **kwargs):
        delete_campaigns = self.send_request(
            "ads.deleteCampaigns", kwargs
        )
        return delete_campaigns

    def delete_clients(self, **kwargs):
        delete_clients = self.send_request(
            "ads.deleteClients", kwargs
        )
        return delete_clients

    def delete_target_group(self, **kwargs):
        delete_target_group = self.send_request(
            "ads.deleteTargetGroup", kwargs
        )
        return delete_target_group

    def delete_target_pixel(self, **kwargs):
        delete_target_pixel = self.send_request(
            "ads.deleteTargetPixel", kwargs
        )
        return delete_target_pixel

    def get_accounts(self, **kwargs):
        get_accounts = self.send_request(
            "ads.getAccounts", kwargs
        )
        return get_accounts

    def get_ads(self, **kwargs):
        get_ads = self.send_request(
            "ads.getAds", kwargs
        )
        return get_ads

    def get_ads_layout(self, **kwargs):
        get_ads_layout = self.send_request(
            "ads.getAdsLayout", kwargs
        )
        return get_ads_layout

    def get_ads_targeting(self, **kwargs):
        get_ads_targeting = self.send_request(
            "ads.getAdsTargeting", kwargs
        )
        return get_ads_targeting

    def get_budget(self, **kwargs):
        get_budget = self.send_request(
            "ads.getBudget", kwargs
        )
        return get_budget

    def get_campaigns(self, **kwargs):
        get_campaigns = self.send_request(
            "ads.getCampaigns", kwargs
        )
        return get_campaigns

    def get_categories(self, **kwargs):
        get_categories = self.send_request(
            "ads.getCategories", kwargs
        )
        return get_categories

    def get_clients(self, **kwargs):
        get_clients = self.send_request(
            "ads.getClients", kwargs
        )
        return get_clients

    def get_demographics(self, **kwargs):
        get_demographics = self.send_request(
            "ads.getDemographics", kwargs
        )
        return get_demographics

    def get_flood_stats(self, **kwargs):
        get_flood_stats = self.send_request(
            "ads.getFloodStats", kwargs
        )
        return get_flood_stats

    def get_look_a_like_requests(self, **kwargs):
        get_look_a_like_requests = self.send_request(
            "ads.getLookalikeRequests", kwargs
        )
        return get_look_a_like_requests

    def get_musicians(self, **kwargs):
        get_musicians = self.send_request(
            "ads.getMusicians", kwargs
        )
        return get_musicians

    def get_musicians_by_ids(self, **kwargs):
        get_musicians_by_ids = self.send_request(
            "ads.getMusiciansByIds", kwargs
        )
        return get_musicians_by_ids

    def get_office_users(self, **kwargs):
        get_office_users = self.send_request(
            "ads.getOfficeUsers", kwargs
        )
        return get_office_users

    def get_posts_reach(self, **kwargs):
        get_posts_reach = self.send_request(
            "ads.getPostsReach", kwargs
        )
        return get_posts_reach

    def get_rejection_reason(self, **kwargs):
        get_rejection_reason = self.send_request(
            "ads.getRejectionReason", kwargs
        )
        return get_rejection_reason

    def get_statistics(self, **kwargs):
        get_statistics = self.send_request(
            "ads.getStatistics", kwargs
        )
        return get_statistics

    def get_suggestions(self, **kwargs):
        get_suggestions = self.send_request(
            "ads.getSuggestions", kwargs
        )
        return get_suggestions

    def get_target_groups(self, **kwargs):
        get_target_groups = self.send_request(
            "ads.getTargetGroups", kwargs
        )
        return get_target_groups

    def get_target_pixels(self, **kwargs):
        get_target_pixels = self.send_request(
            "ads.getTargetPixels", kwargs
        )
        return get_target_pixels

    def get_targeting_stats(self, **kwargs):
        get_targeting_stats = self.send_request(
            "ads.getTargetingStats", kwargs
        )
        return get_targeting_stats

    def get_upload_url(self, **kwargs):
        get_upload_url = self.send_request(
            "ads.getUploadURL", kwargs
        )
        return get_upload_url

    def get_video_upload_url(self, **kwargs):
        get_video_upload_url = self.send_request(
            "ads.getVideoUploadURL", kwargs
        )
        return get_video_upload_url

    def import_target_contacts(self, **kwargs):
        import_target_contacts = self.send_request(
            "ads.importTargetContacts", kwargs
        )
        return import_target_contacts

    def remove_office_users(self, **kwargs):
        remove_office_users = self.send_request(
            "ads.removeOfficeUsers", kwargs
        )
        return remove_office_users

    def remove_target_contacts(self, **kwargs):
        remove_target_contacts = self.send_request(
            "ads.removeTargetContacts", kwargs
        )
        return remove_target_contacts

    def save_look_a_like_request_result(self, **kwargs):
        save_look_a_like_request_result = self.send_request(
            "ads.saveLookalikeRequestResult", kwargs
        )
        return save_look_a_like_request_result

    def share_target_group(self, **kwargs):
        share_target_group = self.send_request(
            "ads.shareTargetGroup", kwargs
        )
        return share_target_group

    def update_ads(self, **kwargs):
        update_ads = self.send_request(
            "ads.updateAds", kwargs
        )
        return update_ads

    def update_campaigns(self, **kwargs):
        update_campaigns = self.send_request(
            "ads.updateCampaigns", kwargs
        )
        return update_campaigns

    def update_clients(self, **kwargs):
        update_clients = self.send_request(
            "ads.updateClients", kwargs
        )
        return update_clients

    def update_office_users(self, **kwargs):
        update_office_users = self.send_request(
            "ads.updateOfficeUsers", kwargs
        )
        return update_office_users

    def update_target_group(self, **kwargs):
        update_target_group = self.send_request(
            "ads.updateTargetGroup", kwargs
        )
        return update_target_group

    def update_target_pixel(self, **kwargs):
        update_target_pixel = self.send_request(
            "ads.updateTargetPixel", kwargs
        )
        return update_target_pixel


class Apps(VkApi):
    def delete_app_requests(self, **kwargs):
        delete_app_requests = self.send_request(
            "apps.deleteAppRequests", kwargs
        )
        return delete_app_requests

    def get(self, **kwargs):
        get_apps = self.send_request(
            "apps.get", kwargs
        )
        return get_apps

    def get_catalog(self, **kwargs):
        get_catalog = self.send_request(
            "apps.getCatalog", kwargs
        )
        return get_catalog

    def get_friends_list(self, **kwargs):
        get_friends_list = self.send_request(
            "apps.getFriendsList", kwargs
        )
        return get_friends_list

    def get_leader_board(self, **kwargs):
        get_leader_board = self.send_request(
            "apps.getLeaderboard", kwargs
        )
        return get_leader_board

    def get_mini_app_policies(self, **kwargs):
        get_mini_app_policies = self.send_request(
            "apps.getMiniAppPolicies", kwargs
        )
        return get_mini_app_policies

    def get_scopes(self, **kwargs):
        get_scopes = self.send_request(
            "apps.getScopes", kwargs
        )
        return get_scopes

    def get_score(self, **kwargs):
        get_score = self.send_request(
            "apps.getScore", kwargs
        )
        return get_score

    def promo_has_active_gift(self, **kwargs):
        promo_has_active_gift = self.send_request(
            "apps.promoHasActiveGift", kwargs
        )
        return promo_has_active_gift

    def promo_use_gift(self, **kwargs):
        promo_use_gift = self.send_request(
            "apps.promoUseGift", kwargs
        )
        return promo_use_gift

    def send_apps_request(self, **kwargs):
        send_apps_request = self.send_request(
            "apps.sendRequest", kwargs
        )
        return send_apps_request


class Board(VkApi):
    def add_topic(self, **kwargs):
        add_topic = self.send_request(
            "board.addTopic", kwargs
        )
        return add_topic

    def close_topic(self, **kwargs):
        close_topic = self.send_request(
            "board.closeTopic", kwargs
        )
        return close_topic

    def create_comment(self, **kwargs):
        create_comment = self.send_request(
            "board.createComment", kwargs
        )
        return create_comment

    def delete_comment(self, **kwargs):
        delete_comment = self.send_request(
            "board.deleteComment", kwargs
        )
        return delete_comment

    def delete_topic(self, **kwargs):
        delete_topic = self.send_request(
            "board.deleteTopic", kwargs
        )
        return delete_topic

    def edit_comment(self, **kwargs):
        edit_comment = self.send_request(
            "board.editComment", kwargs
        )
        return edit_comment

    def edit_topic(self, **kwargs):
        edit_topic = self.send_request(
            "board.editTopic", kwargs
        )
        return edit_topic

    def fix_topic(self, **kwargs):
        fix_topic = self.send_request(
            "board.fixTopic", kwargs
        )
        return fix_topic

    def get_comments(self, **kwargs):
        get_comments = self.send_request(
            "board.getComments", kwargs
        )
        return get_comments

    def get_topics(self, **kwargs):
        get_topics = self.send_request(
            "board.getTopics", kwargs
        )
        return get_topics

    def open_topic(self, **kwargs):
        open_topic = self.send_request(
            "board.openTopic", kwargs
        )
        return open_topic

    def restore_comment(self, **kwargs):
        restore_comment = self.send_request(
            "board.restoreComment", kwargs
        )
        return restore_comment

    def un_fix_topic(self, **kwargs):
        un_fix_topic = self.send_request(
            "board.unfixTopic", kwargs
        )
        return un_fix_topic


class Database(VkApi):
    def get_chairs(self, **kwargs):
        get_chairs = self.send_request(
            "database.getChairs", kwargs
        )
        return get_chairs

    def get_cities(self, **kwargs):
        get_cities = self.send_request(
            "database.getCities", kwargs
        )
        return get_cities

    def get_cities_by_id(self, **kwargs):
        get_cities_by_id = self.send_request(
            "database.getCitiesById", kwargs
        )
        return get_cities_by_id

    def get_countries(self, **kwargs):
        get_countries = self.send_request(
            "database.getCountries", kwargs
        )
        return get_countries

    def get_countries_by_id(self, **kwargs):
        get_countries_by_id = self.send_request(
            "database.getCountriesById", kwargs
        )
        return get_countries_by_id

    def get_faculties(self, **kwargs):
        get_faculties = self.send_request(
            "database.getFaculties", kwargs
        )
        return get_faculties

    def get_metro_stations(self, **kwargs):
        get_metro_stations = self.send_request(
            "database.getMetroStations", kwargs
        )
        return get_metro_stations

    def get_metro_stations_by_id(self, **kwargs):
        get_metro_stations_by_id = self.send_request(
            "database.getMetroStationsById", kwargs
        )
        return get_metro_stations_by_id

    def get_regions(self, **kwargs):
        get_regions = self.send_request(
            "database.getRegions", kwargs
        )
        return get_regions

    def get_school_classes(self, **kwargs):
        get_school_classes = self.send_request(
            "database.getSchoolClasses", kwargs
        )
        return get_school_classes

    def get_schools(self, **kwargs):
        get_schools = self.send_request(
            "database.getSchools", kwargs
        )
        return get_schools

    def get_universities(self, **kwargs):
        get_universities = self.send_request(
            "database.getUniversities", kwargs
        )
        return get_universities


class Docs(VkApi):
    def add(self, **kwargs):
        add = self.send_request(
            "docs.add", kwargs
        )
        return add

    def delete(self, **kwargs):
        delete = self.send_request(
            "docs.delete", kwargs
        )
        return delete

    def edit(self, **kwargs):
        edit = self.send_request(
            "docs.edit", kwargs
        )
        return edit

    def get(self, **kwargs):
        get_docs = self.send_request(
            "docs.get", kwargs
        )
        return get_docs

    def get_by_id(self, **kwargs):
        get_by_id = self.send_request(
            "docs.getById", kwargs
        )
        return get_by_id

    def get_messages_upload_server(self, **kwargs):
        get_messages_upload_server = self.send_request(
            "docs.getMessagesUploadServer", kwargs
        )
        return get_messages_upload_server

    def get_types(self, **kwargs):
        get_types = self.send_request(
            "docs.getTypes", kwargs
        )
        return get_types

    def get_upload_server(self, **kwargs):
        get_upload_server = self.send_request(
            "docs.getUploadServer", kwargs
        )
        return get_upload_server

    def get_wall_upload_server(self, **kwargs):
        get_wall_upload_server = self.send_request(
            "docs.getWallUploadServer", kwargs
        )
        return get_wall_upload_server

    def save(self, **kwargs):
        save = self.send_request(
            "docs.save", kwargs
        )
        return save

    def search(self, **kwargs):
        search = self.send_request(
            "docs.search", kwargs
        )
        return search


class Donut(VkApi):
    def get_friends(self, **kwargs):
        get_friends = self.send_request(
            "donut.getFriends", kwargs
        )
        return get_friends

    def get_subscription(self, **kwargs):
        get_subscription = self.send_request(
            "donut.getSubscription", kwargs
        )
        return get_subscription

    def get_subscriptions(self, **kwargs):
        get_subscriptions = self.send_request(
            "donut.getSubscriptions", kwargs
        )
        return get_subscriptions

    def is_don(self, **kwargs):
        is_don = self.send_request(
            "donut.getSubscriptions", kwargs
        )
        return is_don


class Fave(VkApi):
    def add_article(self, **kwargs):
        add_article = self.send_request(
            "fave.addArticle", kwargs
        )
        return add_article

    def add_link(self, **kwargs):
        add_link = self.send_request(
            "fave.addLink", kwargs
        )
        return add_link

    def add_page(self, **kwargs):
        add_page = self.send_request(
            "fave.addPage", kwargs
        )
        return add_page

    def add_post(self, **kwargs):
        add_post = self.send_request(
            "fave.addPost", kwargs
        )
        return add_post

    def add_product(self, **kwargs):
        add_product = self.send_request(
            "fave.addProduct", kwargs
        )
        return add_product

    def add_tag(self, **kwargs):
        add_tag = self.send_request(
            "fave.addTag", kwargs
        )
        return add_tag

    def add_video(self, **kwargs):
        add_video = self.send_request(
            "fave.addVideo", kwargs
        )
        return add_video

    def edit_tag(self, **kwargs):
        edit_tag = self.send_request(
            "fave.editTag", kwargs
        )
        return edit_tag

    def get(self, **kwargs):
        get_fave = self.send_request(
            "fave.get", kwargs
        )
        return get_fave

    def get_pages(self, **kwargs):
        get_pages = self.send_request(
            "fave.getPages", kwargs
        )
        return get_pages

    def get_tags(self, **kwargs):
        get_tags = self.send_request(
            "fave.getTags", kwargs
        )
        return get_tags

    def mark_seen(self, **kwargs):
        mark_seen = self.send_request(
            "fave.markSeen", kwargs
        )
        return mark_seen

    def remove_article(self, **kwargs):
        remove_article = self.send_request(
            "fave.removeArticle", kwargs
        )
        return remove_article

    def remove_link(self, **kwargs):
        remove_link = self.send_request(
            "fave.removeLink", kwargs
        )
        return remove_link

    def remove_page(self, **kwargs):
        remove_page = self.send_request(
            "fave.removePage", kwargs
        )
        return remove_page

    def remove_post(self, **kwargs):
        remove_post = self.send_request(
            "fave.removePost", kwargs
        )
        return remove_post

    def remove_product(self, **kwargs):
        remove_product = self.send_request(
            "fave.removeProduct", kwargs
        )
        return remove_product

    def remove_tag(self, **kwargs):
        remove_tag = self.send_request(
            "fave.removeTag", kwargs
        )
        return remove_tag

    def remove_video(self, **kwargs):
        remove_video = self.send_request(
            "fave.removeVideo", kwargs
        )
        return remove_video

    def reorder_tags(self, **kwargs):
        reorder_tags = self.send_request(
            "fave.reorderTags", kwargs
        )
        return reorder_tags

    def set_page_tags(self, **kwargs):
        set_page_tags = self.send_request(
            "fave.setPageTags", kwargs
        )
        return set_page_tags

    def set_tags(self, **kwargs):
        set_tags = self.send_request(
            "fave.setTags", kwargs
        )
        return set_tags

    def track_page_interaction(self, **kwargs):
        track_page_interaction = self.send_request(
            "fave.trackPageInteraction", kwargs
        )
        return track_page_interaction


class Friends(VkApi):
    def add(self, **kwargs):
        add = self.send_request(
            "friends.add", kwargs
        )
        return add

    def add_list(self, **kwargs):
        add_list = self.send_request(
            "friends.addList", kwargs
        )
        return add_list

    def are_friends(self, **kwargs):
        are_friends = self.send_request(
            "friends.areFriends", kwargs
        )
        return are_friends

    def delete(self, **kwargs):
        delete = self.send_request(
            "friends.delete", kwargs
        )
        return delete

    def delete_all_requests(self, **kwargs):
        delete_all_requests = self.send_request(
            "friends.deleteAllRequests", kwargs
        )
        return delete_all_requests

    def delete_list(self, **kwargs):
        delete_list = self.send_request(
            "friends.deleteList", kwargs
        )
        return delete_list

    def edit(self, **kwargs):
        edit = self.send_request(
            "friends.edit", kwargs
        )
        return edit

    def edit_list(self, **kwargs):
        edit_list = self.send_request(
            "friends.editList", kwargs
        )
        return edit_list

    def get(self, **kwargs):
        get_friends = self.send_request(
            "friends.get", kwargs
        )
        return get_friends

    def get_app_users(self, **kwargs):
        get_app_users = self.send_request(
            "friends.getAppUsers", kwargs
        )
        return get_app_users

    def get_by_phones(self, **kwargs):
        get_by_phones = self.send_request(
            "friends.getByPhones", kwargs
        )
        return get_by_phones

    def get_lists(self, **kwargs):
        get_lists = self.send_request(
            "friends.getLists", kwargs
        )
        return get_lists

    def get_mutual(self, **kwargs):
        get_mutual = self.send_request(
            "friends.getMutual", kwargs
        )
        return get_mutual

    def get_online(self, **kwargs):
        get_online = self.send_request(
            "friends.getOnline", kwargs
        )
        return get_online

    def get_recent(self, **kwargs):
        get_recent = self.send_request(
            "friends.getRecent", kwargs
        )
        return get_recent

    def get_requests(self, **kwargs):
        get_requests = self.send_request(
            "friends.getRequests", kwargs
        )
        return get_requests

    def get_suggestions(self, **kwargs):
        get_suggestions = self.send_request(
            "friends.getSuggestions", kwargs
        )
        return get_suggestions

    def search(self, **kwargs):
        search = self.send_request(
            "friends.search", kwargs
        )
        return search


class Gifts(VkApi):
    def get(self, **kwargs):
        get_gifts = self.send_request(
            "gifts.get", kwargs
        )
        return get_gifts


class Groups(VkApi):
    def add_address(self, **kwargs):
        add_address = self.send_request(
            "groups.addAddress", kwargs
        )
        return add_address

    def add_callback_server(self, **kwargs):
        add_callback_server = self.send_request(
            "groups.addCallbackServer", kwargs
        )
        return add_callback_server

    def add_link(self, **kwargs):
        add_link = self.send_request(
            "groups.addLink", kwargs
        )
        return add_link

    def approve_request(self, **kwargs):
        approve_request = self.send_request(
            "groups.approveRequest", kwargs
        )
        return approve_request

    def ban(self, **kwargs):
        ban = self.send_request(
            "groups.ban", kwargs
        )
        return ban

    def create(self, **kwargs):
        create = self.send_request(
            "groups.create", kwargs
        )
        return create

    def delete_address(self, **kwargs):
        delete_address = self.send_request(
            "groups.deleteAddress", kwargs
        )
        return delete_address

    def delete_callback_server(self, **kwargs):
        delete_callback_server = self.send_request(
            "groups.deleteCallbackServer", kwargs
        )
        return delete_callback_server

    def delete_link(self, **kwargs):
        delete_link = self.send_request(
            "groups.deleteLink", kwargs
        )
        return delete_link

    def disable_online(self, **kwargs):
        disable_online = self.send_request(
            "groups.disableOnline", kwargs
        )
        return disable_online

    def edit(self, **kwargs):
        edit = self.send_request(
            "groups.edit", kwargs
        )
        return edit

    def edit_address(self, **kwargs):
        edit_address = self.send_request(
            "groups.editAddress", kwargs
        )
        return edit_address

    def edit_callback_server(self, **kwargs):
        edit_callback_server = self.send_request(
            "groups.editCallbackServer", kwargs
        )
        return edit_callback_server

    def edit_link(self, **kwargs):
        edit_link = self.send_request(
            "groups.editLink", kwargs
        )
        return edit_link

    def edit_manager(self, **kwargs):
        edit_manager = self.send_request(
            "groups.editManager", kwargs
        )
        return edit_manager

    def enable_online(self, **kwargs):
        enable_online = self.send_request(
            "groups.enableOnline", kwargs
        )
        return enable_online

    def get(self, **kwargs):
        get_groups = self.send_request(
            "groups.get", kwargs
        )
        return get_groups

    def get_addresses(self, **kwargs):
        get_addresses = self.send_request(
            "groups.getAddresses", kwargs
        )
        return get_addresses

    def get_banned(self, **kwargs):
        get_banned = self.send_request(
            "groups.getBanned", kwargs
        )
        return get_banned

    def get_by_id(self, **kwargs):
        get_by_id = self.send_request(
            "groups.getById", kwargs
        )
        return get_by_id

    def get_callback_confirmation_code(self, **kwargs):
        get_callback_confirmation_code = self.send_request(
            "groups.getCallbackConfirmationCode", kwargs
        )
        return get_callback_confirmation_code

    def get_callback_servers(self, **kwargs):
        get_callback_servers = self.send_request(
            "groups.getCallbackServers", kwargs
        )
        return get_callback_servers

    def get_callback_settings(self, **kwargs):
        get_callback_settings = self.send_request(
            "groups.getCallbackSettings", kwargs
        )
        return get_callback_settings

    def get_catalog(self, **kwargs):
        get_catalog = self.send_request(
            "groups.getCatalog", kwargs
        )
        return get_catalog

    def get_catalog_info(self, **kwargs):
        get_catalog_info = self.send_request(
            "groups.getCatalogInfo", kwargs
        )
        return get_catalog_info

    def get_invited_users(self, **kwargs):
        get_invited_users = self.send_request(
            "groups.getInvitedUsers", kwargs
        )
        return get_invited_users

    def get_invites(self, **kwargs):
        get_invites = self.send_request(
            "groups.getInvites", kwargs
        )
        return get_invites

    def get_longpoll_server(self, **kwargs):
        get_longpoll_server = self.send_request(
            "groups.getLongPollServer", kwargs
        )
        return get_longpoll_server

    def get_longpoll_settings(self, **kwargs):
        get_longpoll_settings = self.send_request(
            "groups.getLongPollSettings", kwargs
        )
        return get_longpoll_settings

    def get_members(self, **kwargs):
        get_members = self.send_request(
            "groups.getMembers", kwargs
        )
        return get_members

    def get_online_status(self, **kwargs):
        get_online_status = self.send_request(
            "groups.getOnlineStatus", kwargs
        )
        return get_online_status

    def get_requests(self, **kwargs):
        get_requests = self.send_request(
            "groups.getRequests", kwargs
        )
        return get_requests

    def get_settings(self, **kwargs):
        get_settings = self.send_request(
            "groups.getSettings", kwargs
        )
        return get_settings

    def get_tag_list(self, **kwargs):
        get_tag_list = self.send_request(
            "groups.getTagList", kwargs
        )
        return get_tag_list

    def get_token_permissions(self, **kwargs):
        get_token_permissions = self.send_request(
            "groups.getTokenPermissions", kwargs
        )
        return get_token_permissions

    def invite(self, **kwargs):
        invite = self.send_request(
            "groups.invite", kwargs
        )
        return invite

    def is_member(self, **kwargs):
        is_member = self.send_request(
            "groups.isMember", kwargs
        )
        return is_member

    def join(self, **kwargs):
        join = self.send_request(
            "groups.join", kwargs
        )
        return join

    def leave(self, **kwargs):
        leave = self.send_request(
            "groups.leave", kwargs
        )
        return leave

    def remove_user(self, **kwargs):
        remove_user = self.send_request(
            "groups.removeUser", kwargs
        )
        return remove_user

    def reorder_link(self, **kwargs):
        reorder_link = self.send_request(
            "groups.reorderLink", kwargs
        )
        return reorder_link

    def search(self, **kwargs):
        search = self.send_request(
            "groups.search", kwargs
        )
        return search

    def set_callback_settings(self, **kwargs):
        set_callback_settings = self.send_request(
            "groups.setCallbackSettings", kwargs
        )
        return set_callback_settings

    def set_longpoll_settings(self, **kwargs):
        set_longpoll_settings = self.send_request(
            "groups.setLongPollSettings", kwargs
        )
        return set_longpoll_settings

    def set_settings(self, **kwargs):
        set_settings = self.send_request(
            "groups.setSettings", kwargs
        )
        return set_settings

    def set_user_note(self, **kwargs):
        set_user_note = self.send_request(
            "groups.setUserNote", kwargs
        )
        return set_user_note

    def tag_add(self, **kwargs):
        tag_add = self.send_request(
            "groups.tagAdd", kwargs
        )
        return tag_add

    def tag_bind(self, **kwargs):
        tag_bind = self.send_request(
            "groups.tagBind", kwargs
        )
        return tag_bind

    def tag_delete(self, **kwargs):
        tag_delete = self.send_request(
            "groups.tagDelete", kwargs
        )
        return tag_delete

    def tag_update(self, **kwargs):
        tag_update = self.send_request(
            "groups.tagUpdate", kwargs
        )
        return tag_update

    def toggle_market(self, **kwargs):
        toggle_market = self.send_request(
            "groups.toggleMarket", kwargs
        )
        return toggle_market

    def unban(self, **kwargs):
        unban = self.send_request(
            "groups.unban", kwargs
        )
        return unban


class Leads(VkApi):
    def ads(self, **kwargs):
        ads = self.send_request(
            "ads", kwargs
        )
        return ads

    def lead_forms(self, **kwargs):
        lead_forms = self.send_request(
            "leadForms", kwargs
        )
        return lead_forms


class Likes(VkApi):
    def add(self, **kwargs):
        add = self.send_request(
            "likes.add", kwargs
        )
        return add

    def delete(self, **kwargs):
        delete = self.send_request(
            "likes.delete", kwargs
        )
        return delete

    def getlist(self, **kwargs):
        getlist = self.send_request(
            "likes.getList", kwargs
        )
        return getlist

    def is_liked(self, **kwargs):
        is_liked = self.send_request(
            "likes.isLiked", kwargs
        )
        return is_liked


class Market(VkApi):
    def add(self, **kwargs):
        add = self.send_request(
            "market.add", kwargs
        )
        return add

    def add_album(self, **kwargs):
        add_album = self.send_request(
            "market.addAlbum", kwargs
        )
        return add_album

    def add_to_album(self, **kwargs):
        add_to_album = self.send_request(
            "market.addToAlbum", kwargs
        )
        return add_to_album

    def create_comment(self, **kwargs):
        create_comment = self.send_request(
            "market.createComment", kwargs
        )
        return create_comment

    def delete(self, **kwargs):
        delete = self.send_request(
            "market.delete", kwargs
        )
        return delete

    def delete_album(self, **kwargs):
        delete_album = self.send_request(
            "market.deleteAlbum", kwargs
        )
        return delete_album

    def delete_comment(self, **kwargs):
        delete_comment = self.send_request(
            "market.deleteComment", kwargs
        )
        return delete_comment

    def edit(self, **kwargs):
        edit = self.send_request(
            "market.edit", kwargs
        )
        return edit

    def edit_album(self, **kwargs):
        edit_album = self.send_request(
            "market.editAlbum", kwargs
        )
        return edit_album

    def edit_comment(self, **kwargs):
        edit_comment = self.send_request(
            "market.editComment", kwargs
        )
        return edit_comment

    def edit_order(self, **kwargs):
        edit_order = self.send_request(
            "market.editOrder", kwargs
        )
        return edit_order

    def get(self, **kwargs):
        get_market = self.send_request(
            "market.get", kwargs
        )
        return get_market

    def get_album_by_id(self, **kwargs):
        get_album_by_id = self.send_request(
            "market.getAlbumById", kwargs
        )
        return get_album_by_id

    def get_albums(self, **kwargs):
        get_albums = self.send_request(
            "market.getAlbums", kwargs
        )
        return get_albums

    def get_by_id(self, **kwargs):
        get_by_id = self.send_request(
            "market.getById", kwargs
        )
        return get_by_id

    def get_categories(self, **kwargs):
        get_categories = self.send_request(
            "market.getCategories", kwargs
        )
        return get_categories

    def get_comments(self, **kwargs):
        get_comments = self.send_request(
            "market.getComments", kwargs
        )
        return get_comments

    def get_group_orders(self, **kwargs):
        get_group_orders = self.send_request(
            "market.getGroupOrders", kwargs
        )
        return get_group_orders

    def get_order_by_id(self, **kwargs):
        get_order_by_id = self.send_request(
            "market.getOrderById", kwargs
        )
        return get_order_by_id

    def get_order_items(self, **kwargs):
        get_order_items = self.send_request(
            "market.getOrderItems", kwargs
        )
        return get_order_items

    def get_orders(self, **kwargs):
        get_orders = self.send_request(
            "market.getOrders", kwargs
        )
        return get_orders

    def remove_from_album(self, **kwargs):
        remove_from_album = self.send_request(
            "market.removeFromAlbum", kwargs
        )
        return remove_from_album

    def reorder_albums(self, **kwargs):
        reorder_albums = self.send_request(
            "market.reorderAlbums", kwargs
        )
        return reorder_albums

    def reorder_items(self, **kwargs):
        reorder_items = self.send_request(
            "market.reorderItems", kwargs
        )
        return reorder_items

    def report(self, **kwargs):
        report = self.send_request(
            "market.report", kwargs
        )
        return report

    def report_comment(self, **kwargs):
        report_comment = self.send_request(
            "market.reportComment", kwargs
        )
        return report_comment

    def restore(self, **kwargs):
        restore = self.send_request(
            "market.restore", kwargs
        )
        return restore

    def restore_comment(self, **kwargs):
        restore_comment = self.send_request(
            "market.restoreComment", kwargs
        )
        return restore_comment

    def search(self, **kwargs):
        search = self.send_request(
            "market.search", kwargs
        )
        return search


class Messages(VkApi):
    def add_chat_user(self, **kwargs):
        add_chat_user = self.send_request(
            "messages.addChatUser", kwargs
        )
        return add_chat_user

    def allow_messages_from_group(self, **kwargs):
        allow_messages_from_group = self.send_request(
            "messages.allowMessagesFromGroup", kwargs
        )
        return allow_messages_from_group

    def create_chat(self, **kwargs):
        create_chat = self.send_request(
            "messages.createChat", kwargs
        )
        return create_chat

    def delete(self, **kwargs):
        delete = self.send_request(
            "messages.delete", kwargs
        )
        return delete

    def delete_chat_photo(self, **kwargs):
        delete_chat_photo = self.send_request(
            "messages.deleteChatPhoto", kwargs
        )
        return delete_chat_photo

    def delete_conversation(self, **kwargs):
        delete_conversation = self.send_request(
            "messages.deleteConversation", kwargs
        )
        return delete_conversation

    def deny_messages_from_group(self, **kwargs):
        deny_messages_from_group = self.send_request(
            "messages.denyMessagesFromGroup", kwargs
        )
        return deny_messages_from_group

    def edit(self, **kwargs):
        edit = self.send_request(
            "messages.edit", kwargs
        )
        return edit

    def edit_chat(self, **kwargs):
        edit_chat = self.send_request(
            "messages.editChat", kwargs
        )
        return edit_chat

    def get_by_conversation_message_id(self, **kwargs):
        get_by_conversation_message_id = self.send_request(
            "messages.getByConversationMessageId", kwargs
        )
        return get_by_conversation_message_id

    def get_by_id(self, **kwargs):
        get_by_id = self.send_request(
            "messages.getById", kwargs
        )
        return get_by_id

    def get_chat(self, **kwargs):
        get_chat = self.send_request(
            "messages.getChat", kwargs
        )
        return get_chat

    def get_chat_preview(self, **kwargs):
        get_chat_preview = self.send_request(
            "messages.getChatPreview", kwargs
        )
        return get_chat_preview

    def get_conversation_members(self, **kwargs):
        get_conversation_members = self.send_request(
            "messages.getConversationMembers", kwargs
        )
        return get_conversation_members

    def get_conversations(self, **kwargs):
        get_conversations = self.send_request(
            "messages.getConversations", kwargs
        )
        return get_conversations

    def get_conversations_by_id(self, **kwargs):
        get_conversations_by_id = self.send_request(
            "messages.getConversationsById", kwargs
        )
        return get_conversations_by_id

    def get_history(self, **kwargs):
        get_history = self.send_request(
            "messages.getHistory", kwargs
        )
        return get_history

    def get_history_attachments(self, **kwargs):
        get_history_attachments = self.send_request(
            "messages.getHistoryAttachments", kwargs
        )
        return get_history_attachments

    def get_important_messages(self, **kwargs):
        get_important_messages = self.send_request(
            "messages.getImportantMessages", kwargs
        )
        return get_important_messages

    def get_intent_users(self, **kwargs):
        get_intent_users = self.send_request(
            "messages.getIntentUsers", kwargs
        )
        return get_intent_users

    def get_invite_link(self, **kwargs):
        get_invite_link = self.send_request(
            "messages.getInviteLink", kwargs
        )
        return get_invite_link

    def get_last_activity(self, **kwargs):
        get_last_activity = self.send_request(
            "messages.getLastActivity", kwargs
        )
        return get_last_activity

    def get_longpoll_history(self, **kwargs):
        get_longpoll_history = self.send_request(
            "messages.getLongPollHistory", kwargs
        )
        return get_longpoll_history

    def get_longpoll_server(self, **kwargs):
        get_longpoll_server = self.send_request(
            "messages.getLongPollServer", kwargs
        )
        return get_longpoll_server

    def is_messages_from_group_allowed(self, **kwargs):
        is_messages_from_group_allowed = self.send_request(
            "messages.isMessagesFromGroupAllowed", kwargs
        )
        return is_messages_from_group_allowed

    def join_chat_by_invite_link(self, **kwargs):
        join_chat_by_invite_link = self.send_request(
            "messages.joinChatByInviteLink", kwargs
        )
        return join_chat_by_invite_link

    def mark_as_answered_conversation(self, **kwargs):
        mark_as_answered_conversation = self.send_request(
            "messages.markAsAnsweredConversation", kwargs
        )
        return mark_as_answered_conversation

    def mark_as_important(self, **kwargs):
        mark_as_important = self.send_request(
            "messages.markAsImportant", kwargs
        )
        return mark_as_important

    def mark_as_important_conversation(self, **kwargs):
        mark_as_important_conversation = self.send_request(
            "messages.markAsImportantConversation", kwargs
        )
        return mark_as_important_conversation

    def mark_as_read(self, **kwargs):
        mark_as_read = self.send_request(
            "messages.markAsRead", kwargs
        )
        return mark_as_read

    def pin(self, **kwargs):
        pin = self.send_request(
            "messages.pin", kwargs
        )
        return pin

    def remove_chat_user(self, **kwargs):
        remove_chat_user = self.send_request(
            "messages.removeChatUser", kwargs
        )
        return remove_chat_user

    def restore(self, **kwargs):
        restore = self.send_request(
            "messages.restore", kwargs
        )
        return restore

    def search(self, **kwargs):
        search = self.send_request(
            "messages.search", kwargs
        )
        return search

    def search_conversations(self, **kwargs):
        search_conversations = self.send_request(
            "messages.searchConversations", kwargs
        )
        return search_conversations

    def send(self, **kwargs):
        send = self.send_request(
            "messages.send", kwargs
        )
        return send

    def send_message_event_answer(self, **kwargs):
        send_message_event_answer = self.send_request(
            "messages.sendMessageEventAnswer", kwargs
        )
        return send_message_event_answer

    def set_activity(self, **kwargs):
        set_activity = self.send_request(
            "messages.setActivity", kwargs
        )
        return set_activity

    def set_chat_photo(self, **kwargs):
        set_chat_photo = self.send_request(
            "messages.setChatPhoto", kwargs
        )
        return set_chat_photo

    def unpin(self, **kwargs):
        unpin = self.send_request(
            "messages.unpin", kwargs
        )
        return unpin


class Newsfeed(VkApi):
    def add_ban(self, **kwargs):
        add_ban = self.send_request(
            "newsfeed.addBan", kwargs
        )
        return add_ban

    def delete_ban(self, **kwargs):
        delete_ban = self.send_request(
            "newsfeed.deleteBan", kwargs
        )
        return delete_ban

    def delete_list(self, **kwargs):
        delete_list = self.send_request(
            "newsfeed.deleteList", kwargs
        )
        return delete_list

    def get(self, **kwargs):
        get_newsfeed = self.send_request(
            "newsfeed.get", kwargs
        )
        return get_newsfeed

    def get_banned(self, **kwargs):
        get_banned = self.send_request(
            "newsfeed.getBanned", kwargs
        )
        return get_banned

    def get_comments(self, **kwargs):
        get_comments = self.send_request(
            "newsfeed.getComments", kwargs
        )
        return get_comments

    def get_lists(self, **kwargs):
        get_lists = self.send_request(
            "newsfeed.getLists", kwargs
        )
        return get_lists

    def get_mentions(self, **kwargs):
        get_mentions = self.send_request(
            "newsfeed.getMentions", kwargs
        )
        return get_mentions

    def get_recommended(self, **kwargs):
        get_recommended = self.send_request(
            "newsfeed.getRecommended", kwargs
        )
        return get_recommended

    def get_suggested_sources(self, **kwargs):
        get_suggested_sources = self.send_request(
            "newsfeed.getSuggestedSources", kwargs
        )
        return get_suggested_sources

    def ignore_item(self, **kwargs):
        ignore_item = self.send_request(
            "newsfeed.ignoreItem", kwargs
        )
        return ignore_item

    def save_list(self, **kwargs):
        save_list = self.send_request(
            "newsfeed.saveList", kwargs
        )
        return save_list

    def search(self, **kwargs):
        search = self.send_request(
            "newsfeed.search", kwargs
        )
        return search

    def unignore_item(self, **kwargs):
        unignore_item = self.send_request(
            "newsfeed.unignoreItem", kwargs
        )
        return unignore_item

    def unsubscribe(self, **kwargs):
        unsubscribe = self.send_request(
            "newsfeed.unsubscribe", kwargs
        )
        return unsubscribe


class Notes(VkApi):
    def add(self, **kwargs):
        add = self.send_request(
            "notes.add", kwargs
        )
        return add

    def create_comment(self, **kwargs):
        create_comment = self.send_request(
            "notes.createComment", kwargs
        )
        return create_comment

    def delete(self, **kwargs):
        delete = self.send_request(
            "notes.delete", kwargs
        )
        return delete

    def delete_comment(self, **kwargs):
        delete_comment = self.send_request(
            "notes.deleteComment", kwargs
        )
        return delete_comment

    def edit(self, **kwargs):
        edit = self.send_request(
            "notes.edit", kwargs
        )
        return edit

    def edit_comment(self, **kwargs):
        edit_comment = self.send_request(
            "notes.editComment", kwargs
        )
        return edit_comment

    def get(self, **kwargs):
        get_notes = self.send_request(
            "notes.get", kwargs
        )
        return get_notes

    def get_by_id(self, **kwargs):
        get_by_id = self.send_request(
            "notes.getById", kwargs
        )
        return get_by_id

    def get_comments(self, **kwargs):
        getcomments = self.send_request(
            "notes.getComments", kwargs
        )
        return getcomments

    def restore_comment(self, **kwargs):
        restore_comment = self.send_request(
            "notes.restoreComment", kwargs
        )
        return restore_comment


class Notifications(VkApi):
    def get(self, **kwargs):
        get_notifications = self.send_request(
            "notifications.get", kwargs
        )
        return get_notifications

    def mark_as_viewed(self, **kwargs):
        mark_as_viewed = self.send_request(
            "notifications.markAsViewed", kwargs
        )
        return mark_as_viewed

    def send_message(self, **kwargs):
        send_message = self.send_request(
            "notifications.sendMessage", kwargs
        )
        return send_message


class Pages(VkApi):
    def clear_cache(self, **kwargs):
        clear_cache = self.send_request(
            "pages.clearCache", kwargs
        )
        return clear_cache

    def get(self, **kwargs):
        get_pages = self.send_request(
            "pages.get", kwargs
        )
        return get_pages

    def get_history(self, **kwargs):
        get_history = self.send_request(
            "pages.getHistory", kwargs
        )
        return get_history

    def get_titles(self, **kwargs):
        get_titles = self.send_request(
            "pages.getTitles", kwargs
        )
        return get_titles

    def get_version(self, **kwargs):
        get_version = self.send_request(
            "pages.getVersion", kwargs
        )
        return get_version

    def parse_wiki(self, **kwargs):
        parse_wiki = self.send_request(
            "pages.parseWiki", kwargs
        )
        return parse_wiki

    def save(self, **kwargs):
        save = self.send_request(
            "pages.save", kwargs
        )
        return save

    def save_access(self, **kwargs):
        save_access = self.send_request(
            "pages.saveAccess", kwargs
        )
        return save_access


class Photos(VkApi):
    def confirm_tag(self, **kwargs):
        confirm_tag = self.send_request(
            "photos.confirmTag", kwargs
        )
        return confirm_tag

    def copy(self, **kwargs):
        copy = self.send_request(
            "photos.copy", kwargs
        )
        return copy

    def create_album(self, **kwargs):
        create_album = self.send_request(
            "photos.createAlbum", kwargs
        )
        return create_album

    def create_comment(self, **kwargs):
        create_comment = self.send_request(
            "photos.createComment", kwargs
        )
        return create_comment

    def delete(self, **kwargs):
        delete = self.send_request(
            "photos.delete", kwargs
        )
        return delete

    def delete_album(self, **kwargs):
        delete_album = self.send_request(
            "photos.deleteAlbum", kwargs
        )
        return delete_album

    def delete_comment(self, **kwargs):
        delete_comment = self.send_request(
            "photos.deleteComment", kwargs
        )
        return delete_comment

    def edit(self, **kwargs):
        edit = self.send_request(
            "photos.edit", kwargs
        )
        return edit

    def edit_album(self, **kwargs):
        edit_album = self.send_request(
            "photos.editAlbum", kwargs
        )
        return edit_album

    def edit_comment(self, **kwargs):
        edit_comment = self.send_request(
            "photos.editComment", kwargs
        )
        return edit_comment

    def get(self, **kwargs):
        get_photos = self.send_request(
            "photos.get", kwargs
        )
        return get_photos

    def get_albums(self, **kwargs):
        get_albums = self.send_request(
            "photos.getAlbums", kwargs
        )
        return get_albums

    def get_albums_count(self, **kwargs):
        get_albums_count = self.send_request(
            "photos.getAlbumsCount", kwargs
        )
        return get_albums_count

    def get_all(self, **kwargs):
        get_all = self.send_request(
            "photos.getAll", kwargs
        )
        return get_all

    def get_all_comments(self, **kwargs):
        get_all_comments = self.send_request(
            "photos.getAllComments", kwargs
        )
        return get_all_comments

    def get_by_id(self, **kwargs):
        get_by_id = self.send_request(
            "photos.getById", kwargs
        )
        return get_by_id

    def get_chat_upload_server(self, **kwargs):
        get_chat_upload_server = self.send_request(
            "photos.getChatUploadServer", kwargs
        )
        return get_chat_upload_server

    def get_comments(self, **kwargs):
        get_comments = self.send_request(
            "photos.getComments", kwargs
        )
        return get_comments

    def get_market_album_upload_server(self, **kwargs):
        get_market_album_upload_server = self.send_request(
            "photos.getMarketAlbumUploadServer", kwargs
        )
        return get_market_album_upload_server

    def get_market_upload_server(self, **kwargs):
        get_market_upload_server = self.send_request(
            "photos.getMarketUploadServer", kwargs
        )
        return get_market_upload_server

    def get_messages_upload_server(self, **kwargs):
        get_messages_upload_server = self.send_request(
            "photos.getMessagesUploadServer", kwargs
        )
        return get_messages_upload_server

    def get_new_tags(self, **kwargs):
        get_new_tags = self.send_request(
            "photos.getNewTags", kwargs
        )
        return get_new_tags

    def get_owner_cover_photo_upload_server(self, **kwargs):
        get_owner_cover_photo_upload_server = self.send_request(
            "photos.getOwnerCoverPhotoUploadServer", kwargs
        )
        return get_owner_cover_photo_upload_server

    def get_owner_photo_upload_server(self, **kwargs):
        get_owner_photo_upload_server = self.send_request(
            "photos.getOwnerPhotoUploadServer", kwargs
        )
        return get_owner_photo_upload_server

    def get_tags(self, **kwargs):
        get_tags = self.send_request(
            "photos.getTags", kwargs
        )
        return get_tags

    def get_upload_server(self, **kwargs):
        get_upload_server = self.send_request(
            "photos.getUploadServer", kwargs
        )
        return get_upload_server

    def get_user_photos(self, **kwargs):
        get_user_photos = self.send_request(
            "photos.getUserPhotos", kwargs
        )
        return get_user_photos

    def get_wall_upload_server(self, **kwargs):
        get_wall_upload_server = self.send_request(
            "photos.getWallUploadServer", kwargs
        )
        return get_wall_upload_server

    def make_cover(self, **kwargs):
        make_cover = self.send_request(
            "photos.makeCover", kwargs
        )
        return make_cover

    def move(self, **kwargs):
        move = self.send_request(
            "photos.move", kwargs
        )
        return move

    def put_tag(self, **kwargs):
        put_tag = self.send_request(
            "photos.putTag", kwargs
        )
        return put_tag

    def remove_tag(self, **kwargs):
        remove_tag = self.send_request(
            "photos.removeTag", kwargs
        )
        return remove_tag

    def reorder_albums(self, **kwargs):
        reorder_albums = self.send_request(
            "photos.reorderAlbums", kwargs
        )
        return reorder_albums

    def reorder_photos(self, **kwargs):
        reorder_photos = self.send_request(
            "photos.reorderPhotos", kwargs
        )
        return reorder_photos

    def report(self, **kwargs):
        report = self.send_request(
            "photos.report", kwargs
        )
        return report

    def report_comment(self, **kwargs):
        report_comment = self.send_request(
            "photos.reportComment", kwargs
        )
        return report_comment

    def restore(self, **kwargs):
        restore = self.send_request(
            "photos.restore", kwargs
        )
        return restore

    def restore_comment(self, **kwargs):
        restore_comment = self.send_request(
            "photos.restoreComment", kwargs
        )
        return restore_comment

    def save(self, **kwargs):
        save = self.send_request(
            "photos.save", kwargs
        )
        return save

    def save_market_album_photo(self, **kwargs):
        save_market_album_photo = self.send_request(
            "photos.saveMarketAlbumPhoto", kwargs
        )
        return save_market_album_photo

    def save_market_photo(self, **kwargs):
        save_market_photo = self.send_request(
            "photos.saveMarketPhoto", kwargs
        )
        return save_market_photo

    def save_messages_photo(self, **kwargs):
        save_messages_photo = self.send_request(
            "photos.saveMessagesPhoto", kwargs
        )
        return save_messages_photo

    def save_owner_cover_photo(self, **kwargs):
        save_owner_cover_photo = self.send_request(
            "photos.saveOwnerCoverPhoto", kwargs
        )
        return save_owner_cover_photo

    def save_owner_photo(self, **kwargs):
        save_owner_photo = self.send_request(
            "photos.saveOwnerPhoto", kwargs
        )
        return save_owner_photo

    def save_wall_photo(self, **kwargs):
        save_wall_photo = self.send_request(
            "photos.saveWallPhoto", kwargs
        )
        return save_wall_photo

    def search(self, **kwargs):
        search = self.send_request(
            "photos.search", kwargs
        )
        return search


class Polls(VkApi):
    def add_vote(self, **kwargs):
        add_vote = self.send_request(
            "polls.addVote", kwargs
        )
        return add_vote

    def create(self, **kwargs):
        create = self.send_request(
            "polls.create", kwargs
        )
        return create

    def delete_vote(self, **kwargs):
        delete_vote = self.send_request(
            "polls.deleteVote", kwargs
        )
        return delete_vote

    def edit(self, **kwargs):
        edit = self.send_request(
            "polls.edit", kwargs
        )
        return edit

    def get_backgrounds(self, **kwargs):
        get_backgrounds = self.send_request(
            "polls.getBackgrounds", kwargs
        )
        return get_backgrounds

    def get_by_id(self, **kwargs):
        get_by_id = self.send_request(
            "polls.getById", kwargs
        )
        return get_by_id

    def get_photo_upload_server(self, **kwargs):
        get_photo_upload_server = self.send_request(
            "polls.getPhotoUploadServer", kwargs
        )
        return get_photo_upload_server

    def get_voters(self, **kwargs):
        get_voters = self.send_request(
            "polls.getVoters", kwargs
        )
        return get_voters

    def save_photo(self, **kwargs):
        save_photo = self.send_request(
            "polls.savePhoto", kwargs
        )
        return save_photo


class Search(VkApi):
    def get_hints(self, **kwargs):
        get_hints = self.send_request(
            "search.getHints", kwargs
        )
        return get_hints


class Secure(VkApi):
    def add_app_event(self, **kwargs):
        add_app_event = self.send_request(
            "secure.addAppEvent", kwargs
        )
        return add_app_event

    def check_token(self, **kwargs):
        check_token = self.send_request(
            "secure.checkToken", kwargs
        )
        return check_token

    def get_app_balance(self, **kwargs):
        get_app_balance = self.send_request(
            "secure.getAppBalance", kwargs
        )
        return get_app_balance

    def get_sms_history(self, **kwargs):
        get_sms_history = self.send_request(
            "secure.getSMSHistory", kwargs
        )
        return get_sms_history

    def get_transactions_history(self, **kwargs):
        get_transactions_history = self.send_request(
            "secure.getTransactionsHistory", kwargs
        )
        return get_transactions_history

    def get_user_level(self, **kwargs):
        get_user_level = self.send_request(
            "secure.getUserLevel", kwargs
        )
        return get_user_level

    def give_event_sticker(self, **kwargs):
        give_event_sticker = self.send_request(
            "secure.giveEventSticker", kwargs
        )
        return give_event_sticker

    def send_notification(self, **kwargs):
        send_notification = self.send_request(
            "secure.sendNotification", kwargs
        )
        return send_notification

    def send_sms_notification(self, **kwargs):
        send_sms_notification = self.send_request(
            "secure.sendSMSNotification", kwargs
        )
        return send_sms_notification

    def set_counter(self, **kwargs):
        set_counter = self.send_request(
            "secure.setCounter", kwargs
        )
        return set_counter


class Stats(VkApi):
    def get(self, **kwargs):
        get_stats = self.send_request(
            "stats.get", kwargs
        )
        return get_stats

    def get_post_reach(self, **kwargs):
        get_post_reach = self.send_request(
            "stats.getPostReach", kwargs
        )
        return get_post_reach

    def track_visitor(self, **kwargs):
        track_visitor = self.send_request(
            "stats.trackVisitor", kwargs
        )
        return track_visitor


class Status(VkApi):
    def get(self, **kwargs):
        get_status = self.send_request(
            "status.get", kwargs
        )
        return get_status

    def set(self, **kwargs):
        set_status = self.send_request(
            "status.set", kwargs
        )
        return set_status


class Storage(VkApi):
    def get(self, **kwargs):
        get_storage = self.send_request(
            "storage.get", kwargs
        )
        return get_storage

    def get_keys(self, **kwargs):
        get_keys = self.send_request(
            "storage.getKeys", kwargs
        )
        return get_keys

    def set(self, **kwargs):
        set_storage = self.send_request(
            "storage.set", kwargs
        )
        return set_storage


class Users(VkApi):
    def get(self, **kwargs):
        get_users = self.send_request(
            "users.get", kwargs
        )
        return get_users

    def get_followers(self, **kwargs):
        get_followers = self.send_request(
            "users.getFollowers", kwargs
        )
        return get_followers

    def get_subscriptions(self, **kwargs):
        get_subscriptions = self.send_request(
            "users.getSubscriptions", kwargs
        )
        return get_subscriptions

    def report(self, **kwargs):
        report = self.send_request(
            "users.report", kwargs
        )
        return report

    def search(self, **kwargs):
        search = self.send_request(
            "users.search", kwargs
        )
        return search


class Utils(VkApi):
    def check_link(self, **kwargs):
        check_link = self.send_request(
            "utils.checkLink", kwargs
        )
        return check_link

    def delete_from_last_shortened(self, **kwargs):
        delete_from_last_shortened = self.send_request(
            "utils.deleteFromLastShortened", kwargs
        )
        return delete_from_last_shortened

    def get_last_shortened_links(self, **kwargs):
        get_last_shortened_links = self.send_request(
            "utils.getLastShortenedLinks", kwargs
        )
        return get_last_shortened_links

    def get_link_stats(self, **kwargs):
        get_link_stats = self.send_request(
            "utils.getLinkStats", kwargs
        )
        return get_link_stats

    def get_server_time(self, **kwargs):
        get_server_time = self.send_request(
            "utils.getServerTime", kwargs
        )
        return get_server_time

    def get_short_link(self, **kwargs):
        get_short_link = self.send_request(
            "utils.getShortLink", kwargs
        )
        return get_short_link

    def resolve_screen_name(self, **kwargs):
        resolve_screen_name = self.send_request(
            "utils.resolveScreenName", kwargs
        )
        return resolve_screen_name


class Video(VkApi):
    def add(self, **kwargs):
        add = self.send_request(
            "video.add", kwargs
        )
        return add

    def add_album(self, **kwargs):
        add_album = self.send_request(
            "video.addAlbum", kwargs
        )
        return add_album

    def add_to_album(self, **kwargs):
        add_to_album = self.send_request(
            "video.addToAlbum", kwargs
        )
        return add_to_album

    def create_comment(self, **kwargs):
        create_comment = self.send_request(
            "video.createComment", kwargs
        )
        return create_comment

    def delete(self, **kwargs):
        delete = self.send_request(
            "video.delete", kwargs
        )
        return delete

    def delete_album(self, **kwargs):
        delete_album = self.send_request(
            "video.deleteAlbum", kwargs
        )
        return delete_album

    def delete_comment(self, **kwargs):
        delete_comment = self.send_request(
            "video.deleteComment", kwargs
        )
        return delete_comment

    def edit(self, **kwargs):
        edit = self.send_request(
            "video.edit", kwargs
        )
        return edit

    def edit_album(self, **kwargs):
        edit_album = self.send_request(
            "video.editAlbum", kwargs
        )
        return edit_album

    def edit_comment(self, **kwargs):
        edit_comment = self.send_request(
            "video.editComment", kwargs
        )
        return edit_comment

    def get(self, **kwargs):
        get_video = self.send_request(
            "video.get", kwargs
        )
        return get_video

    def get_album_byid(self, **kwargs):
        get_album_by_id = self.send_request(
            "video.getAlbumById", kwargs
        )
        return get_album_by_id

    def get_albums(self, **kwargs):
        get_albums = self.send_request(
            "video.getAlbums", kwargs
        )
        return get_albums

    def get_albums_by_video(self, **kwargs):
        get_albums_by_video = self.send_request(
            "video.getAlbumsByVideo", kwargs
        )
        return get_albums_by_video

    def get_comments(self, **kwargs):
        get_comments = self.send_request(
            "video.getComments", kwargs
        )
        return get_comments

    def remove_from_album(self, **kwargs):
        remove_from_album = self.send_request(
            "video.removeFromAlbum", kwargs
        )
        return remove_from_album

    def reorder_albums(self, **kwargs):
        reorder_albums = self.send_request(
            "video.reorderAlbums", kwargs
        )
        return reorder_albums

    def reorder_videos(self, **kwargs):
        reorder_videos = self.send_request(
            "video.reorderVideos", kwargs
        )
        return reorder_videos

    def report(self, **kwargs):
        report = self.send_request(
            "video.report", kwargs
        )
        return report

    def report_comment(self, **kwargs):
        report_comment = self.send_request(
            "video.reportComment", kwargs
        )
        return report_comment

    def restore(self, **kwargs):
        restore = self.send_request(
            "video.restore", kwargs
        )
        return restore

    def restore_comment(self, **kwargs):
        restore_comment = self.send_request(
            "video.restoreComment", kwargs
        )
        return restore_comment

    def save(self, **kwargs):
        save = self.send_request(
            "video.save", kwargs
        )
        return save

    def search(self, **kwargs):
        search = self.send_request(
            "video.search", kwargs
        )
        return search


class Podcasts(VkApi):
    def search_podcast(self, **kwargs):
        search_podcast = self.send_request(
            "podcasts.searchPodcast", kwargs
        )
        return search_podcast


class Leadforms(VkApi):
    def lead_forms(self, **kwargs):
        lead_forms = self.send_request(
            "leadForms", kwargs
        )
        return lead_forms


class Prettycards(VkApi):
    def pretty_cards(self, **kwargs):
        pretty_cards = self.send_request(
            "prettyCards", kwargs
        )
        return pretty_cards


class Stories(VkApi):
    def ban_owner(self, **kwargs):
        ban_owner = self.send_request(
            "stories.banOwner", kwargs
        )
        return ban_owner

    def delete(self, **kwargs):
        delete = self.send_request(
            "stories.delete", kwargs
        )
        return delete

    def get(self, **kwargs):
        get_stories = self.send_request(
            "stories.get", kwargs
        )
        return get_stories

    def get_banned(self, **kwargs):
        get_banned = self.send_request(
            "stories.getBanned", kwargs
        )
        return get_banned

    def get_by_id(self, **kwargs):
        get_by_id = self.send_request(
            "stories.getById", kwargs
        )
        return get_by_id

    def get_photo_upload_server(self, **kwargs):
        get_photo_upload_server = self.send_request(
            "stories.getPhotoUploadServer", kwargs
        )
        return get_photo_upload_server

    def get_replies(self, **kwargs):
        get_replies = self.send_request(
            "stories.getReplies", kwargs
        )
        return get_replies

    def get_stats(self, **kwargs):
        get_stats = self.send_request(
            "stories.getStats", kwargs
        )
        return get_stats

    def get_video_upload_server(self, **kwargs):
        get_video_upload_server = self.send_request(
            "stories.getVideoUploadServer", kwargs
        )
        return get_video_upload_server

    def get_viewers(self, **kwargs):
        get_viewers = self.send_request(
            "stories.getViewers", kwargs
        )
        return get_viewers

    def hide_all_replies(self, **kwargs):
        hide_all_replies = self.send_request(
            "stories.hideAllReplies", kwargs
        )
        return hide_all_replies

    def hide_reply(self, **kwargs):
        hide_reply = self.send_request(
            "stories.hideReply", kwargs
        )
        return hide_reply

    def save(self, **kwargs):
        save = self.send_request(
            "stories.save", kwargs
        )
        return save

    def search(self, **kwargs):
        search = self.send_request(
            "stories.search", kwargs
        )
        return search

    def send_interaction(self, **kwargs):
        send_interaction = self.send_request(
            "stories.sendInteraction", kwargs
        )
        return send_interaction

    def un_ban_owner(self, **kwargs):
        un_ban_owner = self.send_request(
            "stories.unbanOwner", kwargs
        )
        return un_ban_owner


class Appwidgets(VkApi):
    def app_widgets(self, **kwargs):
        app_widgets = self.send_request(
            "appWidgets", kwargs
        )
        return app_widgets

    def widgets(self, **kwargs):
        widgets = self.send_request(
            "widgets", kwargs
        )
        return widgets


class Streaming(VkApi):
    def get_server_url(self, **kwargs):
        get_server_url = self.send_request(
            "streaming.getServerUrl", kwargs
        )
        return get_server_url

    def get_settings(self, **kwargs):
        get_settings = self.send_request(
            "streaming.getSettings", kwargs
        )
        return get_settings

    def get_stats(self, **kwargs):
        get_stats = self.send_request(
            "streaming.getStats", kwargs
        )
        return get_stats

    def get_stem(self, **kwargs):
        get_stem = self.send_request(
            "streaming.getStem", kwargs
        )
        return get_stem

    def set_settings(self, **kwargs):
        set_settings = self.send_request(
            "streaming.setSettings", kwargs
        )
        return set_settings


class Orders(VkApi):
    def cancel_subscription(self, **kwargs):
        cancel_subscription = self.send_request(
            "orders.cancelSubscription", kwargs
        )
        return cancel_subscription

    def change_state(self, **kwargs):
        change_state = self.send_request(
            "orders.changeState", kwargs
        )
        return change_state

    def get(self, **kwargs):
        get_orders = self.send_request(
            "orders.get", kwargs
        )
        return get_orders

    def get_amount(self, **kwargs):
        get_amount = self.send_request(
            "orders.getAmount", kwargs
        )
        return get_amount

    def get_by_id(self, **kwargs):
        get_by_id = self.send_request(
            "orders.getById", kwargs
        )
        return get_by_id

    def get_user_subscription_by_id(self, **kwargs):
        get_user_subscription_by_id = self.send_request(
            "orders.getUserSubscriptionById", kwargs
        )
        return get_user_subscription_by_id

    def get_user_subscriptions(self, **kwargs):
        get_user_subscriptions = self.send_request(
            "orders.getUserSubscriptions", kwargs
        )
        return get_user_subscriptions

    def update_subscription(self, **kwargs):
        update_subscription = self.send_request(
            "orders.updateSubscription", kwargs
        )
        return update_subscription


class Wall(VkApi):
    def check_copyright_link(self, **kwargs):
        check_copyright_link = self.send_request(
            "wall.checkCopyrightLink", kwargs
        )
        return check_copyright_link

    def close_comments(self, **kwargs):
        close_comments = self.send_request(
            "wall.closeComments", kwargs
        )
        return close_comments

    def create_comment(self, **kwargs):
        create_comment = self.send_request(
            "wall.createComment", kwargs
        )
        return create_comment

    def delete(self, **kwargs):
        delete = self.send_request(
            "wall.delete", kwargs
        )
        return delete

    def delete_comment(self, **kwargs):
        delete_comment = self.send_request(
            "wall.deleteComment", kwargs
        )
        return delete_comment

    def edit(self, **kwargs):
        edit = self.send_request(
            "wall.edit", kwargs
        )
        return edit

    def edit_ads_stealth(self, **kwargs):
        edit_ads_stealth = self.send_request(
            "wall.editAdsStealth", kwargs
        )
        return edit_ads_stealth

    def edit_comment(self, **kwargs):
        edit_comment = self.send_request(
            "wall.editComment", kwargs
        )
        return edit_comment

    def get(self, **kwargs):
        get_wall = self.send_request(
            "wall.get", kwargs
        )
        return get_wall

    def get_by_id(self, **kwargs):
        get_by_id = self.send_request(
            "wall.getById", kwargs
        )
        return get_by_id

    def get_comment(self, **kwargs):
        getcomment = self.send_request(
            "wall.getComment", kwargs
        )
        return getcomment

    def get_comments(self, **kwargs):
        getcomments = self.send_request(
            "wall.getComments", kwargs
        )
        return getcomments

    def get_reposts(self, **kwargs):
        get_reposts = self.send_request(
            "wall.getReposts", kwargs
        )
        return get_reposts

    def open_comments(self, **kwargs):
        open_comments = self.send_request(
            "wall.openComments", kwargs
        )
        return open_comments

    def pin(self, **kwargs):
        pin_post = self.send_request(
            "wall.pin", kwargs
        )
        return pin_post

    def post(self, **kwargs):
        post = self.send_request(
            "wall.post", kwargs
        )
        return post

    def post_ads_stealth(self, **kwargs):
        post_ads_stealth = self.send_request(
            "wall.postAdsStealth", kwargs
        )
        return post_ads_stealth

    def report_comment(self, **kwargs):
        report_comment = self.send_request(
            "wall.reportComment", kwargs
        )
        return report_comment

    def report_post(self, **kwargs):
        report_post = self.send_request(
            "wall.reportPost", kwargs
        )
        return report_post

    def repost(self, **kwargs):
        repost = self.send_request(
            "wall.repost", kwargs
        )
        return repost

    def restore(self, **kwargs):
        restore = self.send_request(
            "wall.restore", kwargs
        )
        return restore

    def restore_comment(self, **kwargs):
        restore_comment = self.send_request(
            "wall.restoreComment", kwargs
        )
        return restore_comment

    def search(self, **kwargs):
        search = self.send_request(
            "wall.search", kwargs
        )
        return search

    def un_pin(self, **kwargs):
        un_pin = self.send_request(
            "wall.unpin", kwargs
        )
        return un_pin


class Widgets(VkApi):
    def get_comments(self, **kwargs):
        get_comments = self.send_request(
            "widgets.getComments", kwargs
        )
        return get_comments

    def get_pages(self, **kwargs):
        get_pages = self.send_request(
            "widgets.getPages", kwargs
        )
        return get_pages
