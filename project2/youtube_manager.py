# python manager using mongodb

import pymongo


client = pymongo.MongoClient("mongodb+srv://<youtubepy>:<youtubepy>@cluster0.pjxc15s.mongodb.net/ytmanager")

db = client["ytmanager"]
video_collections = db["videos"]

print(video_collections)

def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all youtube videos: ")
        print("2. Add a youtube video: ")
        print("3. Update a youtube video details: ")
        print("4. Delete a youtube video: ")
        print("5. Exit the app. ")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos() 
        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video length: ")
            add_video(name, time)
        elif choice == "3":
            video_id = int(input("Enter the video ID to update: "))
            name = input("Enter new video name: ")
            time = input("Enter new video length: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = int(input("Enter the video ID to update: "))
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()