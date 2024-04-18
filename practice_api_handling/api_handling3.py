import requests
import webbrowser

baseurl = "https://api.freeapi.app/api/v1/public/youtube/videos?page=1&limit=10&query=javascript&sortBy=keep%20one%3A%20mostLiked%20%7C%20mostViewed%20%7C%20latest%20%7C%20oldest"

r = requests.get(baseurl)

# print(r) # 200 is response 400 and 404 is not response and 500 is access denied

data = r.json()
# print(data['info']) # {'count': 826, 'pages': 42, 'next': 'https://rickandmortyapi.com/api/character?page=2', 'prev': None}
# print(data['info']['pages']) # 42

# list or array and [0] is first item
name = data['data']['data'][0]['items']['snippet']['channelId'] # Rick Sanchez

# episodes = data['results'][0]['episode'][0] # first episode

print(f"\nEpisode: {name}")

webbrowser.open("https://www.youtube.com/results?search_query=" + name)