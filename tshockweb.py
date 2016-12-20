import json
from functools import wraps
from thw.helpers.decorators import pack
from thw.helpers.system import SystemHelper
from thw.helpers.api import TSHOCKClient, HttpException
from flask import Flask, send_from_directory, request, redirect, jsonify


with open('config/tshockweb.json') as settings_file:
    settings = json.load(settings_file)

app = Flask(__name__, static_folder=settings['tshock_web']['web']['base_location'])
API_BASE_PATH = "/api"


def authenicate(func):
    """
    Authenticate the provided token

    :param func: function
    :type func: Function
    """

    @wraps(func)
    def validate(*args, **kwargs):
        try:
            content = request.json
            if content is not None and 'token' in content:
                TSHOCKClient(ip=settings['tshock_server']['host'],
                             port=settings['tshock_server']['port'], token=content['token'])
            else:
                raise HttpException(403, 'No token provided')
            return func(*args, **kwargs)
        except (HttpException, RuntimeError) as ex:
            return jsonify({'status': 403, 'result': ex.message, 'valid': False})

    return validate


@app.route(API_BASE_PATH)
@pack
def base():
    return 'The TSHOCK WEB API is working!', 200


@app.route(API_BASE_PATH + "/config")
@pack
def config():
    return settings, 200


@app.route(API_BASE_PATH + "/login")
@pack
def login():
    """
    Login into the TSHOCK server

    :param username: username of existing user
    :type username: str
    :param password: password of existing user
    :type password: str
    :return:
    """
    content = request.json
    try:
        if content is not None:
            if 'username' in content and 'password' in content:
                api = TSHOCKClient(ip=settings['tshock_server']['host'], port=settings['tshock_server']['port'],
                                   username=content['username'], password=content['password'])
                return {'token': api.token()}, 200
            else:
                raise HttpException(403, 'No username/password provided')
        else:
            raise HttpException(403, 'No username/password provided')
    except (HttpException, RuntimeError) as ex:
        return str(ex.message), 403


@app.route(API_BASE_PATH + "/validate")
@authenicate
@pack
def validate():
    """
    Validate token on TSHOCK server

    :return:
    """
    return 'The given token is valid!', 200


@app.route(API_BASE_PATH + "/documentation")
@pack
def documentation():
    """
    Documentation generator that generates the API documentation

    @TODO: list argument names of every function with:
               * FUNCTION.func_code.co_varnames
               * FUNCTION.func_code.co_argcount

    :return:
    """
    docs = {}

    for directory in SystemHelper.list_directories(settings['tshock_web']['api']['base']):
        subdirs = SystemHelper.list_directories('{0}/{1}'.format(settings['tshock_web']['api']['base'], directory))
        if len(subdirs) != 0:
            for subdir in subdirs:
                temp_subdir = {}
                files = SystemHelper.list_files(path='{0}/{1}/{2}'.format(settings['tshock_web']['api']['base'],
                                                                          directory, subdir), remove_suffix=True)
                for filename in files:
                    temp_subdir[filename] = SystemHelper.list_methods_of_module(path='{0}/{1}/{2}/{3}.py'.format(
                        settings['tshock_web']['api']['base'], directory, subdir, filename), module_name=filename)

                docs[directory] = temp_subdir
        else:
            temp_subdir = {}
            files = SystemHelper.list_files(path='{0}/{1}'.format(settings['tshock_web']['api']['base'],
                                                                  directory), remove_suffix=True)
            for filename in files:
                temp_subdir[filename] = SystemHelper.list_methods_of_module(path='{0}/{1}/{2}.py'.format(
                    settings['tshock_web']['api']['base'], directory, filename), module_name=filename)
            docs[directory] = temp_subdir

    return docs, 200


@app.route(API_BASE_PATH + "/<path:path>")
@authenicate
@pack
def serve_api(path):
    seperated_path = path.split('/')

    content = request.json
    api = TSHOCKClient(ip=settings['tshock_server']['host'], port=settings['tshock_server']['port'],
                       token=content['token'])

    # parse api path
    api_path = path.replace('/' + seperated_path[-1], '')

    # fetch class
    current_class = SystemHelper.get_class_by_path(path="{0}/{1}.py".format(settings['tshock_web']['api']['base'],
                                                                            api_path),
                                                   module_name=seperated_path[-2])
    # remove token and add api
    del content['token']
    content['api'] = api

    # fetch method
    method = getattr(current_class, seperated_path[-1])

    try:
        result = method(**content)
        return {'api_path': api_path,
                'method': seperated_path[-1],
                'output': result}, 200
    except TypeError as ex:
        # remove api argument because its not needed as we pass a token
        arguments = [argument for argument in list(method.func_code.co_varnames) if 'api' not in argument]
        return {'api_path': api_path,
                'method': seperated_path[-1],
                'output': str(ex.message + ',' + ' required arguments: ' + str(arguments))}, 404


@app.route('/<path:filename>')
def serve_files(filename):
    return send_from_directory(app.static_folder, filename)


@app.route('/')
def serve_homepage():
    return redirect(settings['tshock_web']['web']['base_location'] + '/' + settings['tshock_web']['web']['homepage'])


if __name__ == "__main__":
    app.run(host=settings['tshock_web']['api']['host'], port=settings['tshock_web']['api']['port'],
            debug=settings['tshock_web']['api']['debug'])
