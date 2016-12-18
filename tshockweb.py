import json
from thw.helpers.decorators import pack
from flask import Flask, send_from_directory


with open('config/tshockweb.json') as settings_file:
    settings = json.load(settings_file)

app = Flask(__name__, static_folder=settings['tshock_web']['web']['location'])
API_BASE_PATH = "/api"


@app.route(API_BASE_PATH)
@pack
def base():
    return 'The TSHOCK WEB API is working!', 200


@app.route(API_BASE_PATH + "/config")
@pack
def config():
    return settings, 200


@app.route(API_BASE_PATH + "/thw/<api>")
@pack
def serve_api(api):
    return {'api_path': api}, 200


@app.route('/<path:filename>')
def serve_files(filename):
    return send_from_directory(app.static_folder, filename)


if __name__ == "__main__":
    app.run(host=settings['tshock_web']['api']['host'], port=settings['tshock_web']['api']['port'],
            debug=settings['tshock_web']['api']['debug'])
