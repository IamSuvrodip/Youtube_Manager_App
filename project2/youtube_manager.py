# python manager using mongodb

import pymongo


client = pymongo.MongoClient("mongodb+srv://<youtubepy>:<youtubepy>@cluster0.pjxc15s.mongodb.net/ytmanager")

db = client["ytmanager"]
video_collections = db["videos"]

print(video_collections)