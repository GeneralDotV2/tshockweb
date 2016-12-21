import json
import requests

#print requests.post('http://127.0.0.1:14789/api/login').text
#print requests.post('http://127.0.0.1:14789/api/login', json={"username": None, "password": None}).text
print requests.post('http://127.0.0.1:14789/api/login', json={"username": "uperadmin-username", "password": "superadmin-password"}).text

response = json.loads(requests.post('http://127.0.0.1:14789/api/login',
                                    json={"username": "superadmin-username", "password": "superadmin-password"}).text)
print response
#print requests.post('http://127.0.0.1:14789/api/validate', json={"token": response['result']['token']}).text
#print requests.post('http://127.0.0.1:14789/api/model/lists/get_current_players').text
print requests.post('http://127.0.0.1:14789/api/model/lists/players/get_current_players',
                    json={"token": response['result']['token']}).text
#print requests.post('http://127.0.0.1:14789/api/model/lists/groups/get_groups',
#                   json={"token": response['result']['token']}).text
#print requests.post('http://127.0.0.1:14789/api/model/lists/groups/get_group_by_name',
#                   json={"token": response['result']['token'], "group_name": "guest"}).text
print requests.post('http://127.0.0.1:14789/api/model/lists/groups/get_group_by_name',
                    json={"token": response['result']['token']}).text
#print requests.post('http://127.0.0.1:14789/api/config').text
#print requests.post('http://127.0.0.1:14789/api').text
#print requests.post('http://127.0.0.1:14789/api/documentation').text
