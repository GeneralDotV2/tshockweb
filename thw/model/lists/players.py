from thw.helpers.api import TSHOCKClient


class PlayerList(object):
    """
    Represents the lists for players
    """

    @staticmethod
    def get_current_players(api):
        """
        Get players

        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        """

        return api.get(path="players/list")['players']

    @staticmethod
    def get_banned_players(api):
        """
        Get banned players

        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        """

        return api.get(path="bans/list")['bans']

    @staticmethod
    def get_user_in_database(api, username):
        """
        Get user details by username

        :param api: tshock client api
        :type api: TSHOCKClient
        :param username: username of a existing user
        :type username:
        :return:
        """

        return api.get(path="users/read", params={'user': username})

    @staticmethod
    def get_user_in_world(api, username):
        """
        Get information for a user who's playing ingame

        :param api: tshock client api
        :type api: TSHOCKClient
        :param username: username of a existing user
        :type username:
        :return:
        """

        return api.get(path="players/read", params={'player': username}, version='v3')
