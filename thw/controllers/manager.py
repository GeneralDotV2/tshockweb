from thw.helpers.api import TSHOCKClient


class ManagerController(object):
    """
    Represents the controller for Manager
    """

    @staticmethod
    def execute_cmd(api, command):
        """
        Execute a command on the server

        :param api: tshock client api
        :type api: TSHOCKClient
        :param command: the command and arguments to execute
        :type command: str
        :return: dict
        """

        return api.get(path="server/rawcmd", params={'cmd': command}, version='v3')['response']
