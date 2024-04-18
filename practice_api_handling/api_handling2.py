# https://youtu.be/-oPuGc05Lxs

import requests

baseurl = "https://rickandmortyapi.com/api/character"

r = requests.get(baseurl)

# print(r) # 200 is response 400 and 404 is not response and 500 is access denied

data = r.json()
# print(data['info']) # {'count': 826, 'pages': 42, 'next': 'https://rickandmortyapi.com/api/character?page=2', 'prev': None}
# print(data['info']['pages']) # 42

# list or array and [0] is first item
name = data['results'][0]['name'] # Rick Sanchez

episodes = data['results'][0]['episode'][0] # first episode

print(f"\nEpisode: {episodes}")

