# https://youtu.be/-oPuGc05Lxs

import requests
import pandas as pd
baseurl = "https://rickandmortyapi.com/api/character"

def main_response(baseurl, x):
    r = requests.get(baseurl + f'?page= {x}')
    return r.json()

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    charlist = []
    for item in response['results']:
        char = {
            "id": item['id'],
            "name": item['name'], 
            "no_episodes": len(item['episode']),
        }

        charlist.append(char)
    return charlist

# print(data['info']) # {'count': 826, 'pages': 42, 'next': 'https://rickandmortyapi.com/api/character?page=2', 'prev': None}
# print(data['info']['pages']) # 42

mainlist = []
data = main_response(baseurl, 1)
for x in range(1, get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_response(baseurl, x)))


df = pd.DataFrame(mainlist)

df.to_csv('charlist.csv', index = False)
# print(parse_json(data))




























'''import requests

baseurl = "https://rickandmortyapi.com/api/character"

r = requests.get(baseurl)

# print(r) # 200 is response 400 and 404 is not response and 500 is access denied

data = r.json()
# print(data['info']) # {'count': 826, 'pages': 42, 'next': 'https://rickandmortyapi.com/api/character?page=2', 'prev': None}
# print(data['info']['pages']) # 42

# list or array and [0] is first item
name = data['results'][0]['name'] # Rick Sanchez

episodes = data['results'][0]['episode'][0] # first episode

print(f"\nEpisode: {episodes}")'''

