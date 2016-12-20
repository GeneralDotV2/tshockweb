import json
import requests

username = "Kinvaris"
password = "CEmoh534"

#print requests.get('http://127.0.0.1:14789/api/login').text
#print requests.get('http://127.0.0.1:14789/api/login', json={"username": None, "password": None}).text
#print requests.get('http://127.0.0.1:14789/api/login', json={"username": "", "password": ""}).text

response = json.loads(requests.get('http://127.0.0.1:14789/api/login',
                                   json={"username": username, "password": password}).text)
print response
#print requests.get('http://127.0.0.1:14789/api/validate', json={"token": response['result']['token']}).text
#print requests.get('http://127.0.0.1:14789/api/model/lists/get_current_players').text
print requests.get('http://127.0.0.1:14789/api/model/lists/players/get_current_players',
                   json={"token": response['result']['token']}).text
#print requests.get('http://127.0.0.1:14789/api/model/lists/groups/get_groups',
#                   json={"token": response['result']['token']}).text
#print requests.get('http://127.0.0.1:14789/api/model/lists/groups/get_group_by_name',
#                   json={"token": response['result']['token'], "group_name": "guest"}).text
print requests.get('http://127.0.0.1:14789/api/model/lists/groups/get_group_by_name',
                   json={"token": response['result']['token']}).text
#print requests.get('http://127.0.0.1:14789/api/config').text
#print requests.get('http://127.0.0.1:14789/api').text
#print requests.get('http://127.0.0.1:14789/api/documentation').text
