# TSHOCK WEB

## Description
This is the new, improved & lightweight version of the TSHOCK WEB

## Requirements
* `Flask`: `0.11.1`
* `timeout-decorator`: `0.3.2`
* `python-pip`: `1.5.6-5`
* `Python-2.7`

## Easy deployment
* Edit the following config file: `config/tshockweb.json`
* The `tshock_web` section contains the `api` and `web` settings
* The `tshock_server` section contains the settings to the tshock terraria server
* Execute as: `python tshockweb.py`
* Visit the following pages to validate the workability: `http://127.0.0.1:14789/api` & `http://127.0.0.1:14789/html/dashboards/dashboard.html`

## Development
* Easy python API:
```
from thw.model.lists.players import PlayerList
from thw.helpers.api import TSHOCKClient

api = TSHOCKClient(ip="tshock-api-url", port=7878, username='superadmin-username', password='superadmin-password')
print PlayerList.get_current_players(api=api)
```
* Easy REST API: `http://127.0.0.1:14789/api/config`


