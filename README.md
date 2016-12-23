# TSHOCK WEB V2

## Description
This is the new, improved & lightweight version of the TSHOCK WEB

## Status
Currently in alpha

## Requirements
* `Flask`: `0.11.1`
* `python-pip`: `1.5.6-5`
* `Python-2.7`

## Easy deployment
* Edit the following config file: `config/tshockweb.json`
* The `tshock_web` section contains the `api` and `web` settings
* The `tshock_server` section contains the settings to the tshock terraria server
* Execute as: `python tshockweb.py`
* Visit the following pages to validate the workability: `http://127.0.0.1:14789` & `http://127.0.0.1:14789/api`

## GUI

* Easily manage your tshockweb with account(s) that have `superadmin` rights
![](http://i.imgur.com/PiXO1kj.png)

* Easily monitor your tshock terraria server with the dashboard
![](http://i.imgur.com/5gWbJZF.png)

* Easily manage your raw tshock commands with an online command tool
![](http://i.imgur.com/KvoGAdC.jpg)


## Development
* Easy python API:
```
from thw.model.lists.players import PlayerList
from thw.helpers.api import TSHOCKClient

api = TSHOCKClient(ip="tshock-api-url", port=7878, username='superadmin-username', password='superadmin-password')
print PlayerList.get_current_players(api=api)
```

* Easy REST API: 
```
import requests

requests.get('http://127.0.0.1:14789/api/login', json={"username": "superadmin-username", "password": "superadmin-password"}
{
  "result": {
    "token": "B542D501E90A62615F257BCCC47996B4597BAF0E06C9BB727785FFB880CA6F9E"
  }, 
  "status": 200, 
  "valid": true
}

requests.get('http://127.0.0.1:14789/api/model/lists/players/get_current_players', json={"token": "B542D501E90A62615F257BCCC47996B4597BAF0E06C9BB727785FFB880CA6F9E"})
{
  "result": {
    "api_path": "model/lists/players", 
    "method": "get_current_players", 
    "output": []
  }, 
  "status": 200, 
  "valid": true
}

curl -H "Content-Type: application/json" -X GET -d '{"username":"superadmin-username","password":"superadmin-password"}' http://localhost:14789/api/login
```

* Default JSON output:
```
{
  "result": {},  // result of the api call
  "status": 200, // status code of tshockweb api call
  "valid": true  // is valid call to the tshock terraria server
}
```
