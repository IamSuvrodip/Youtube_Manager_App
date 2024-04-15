import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL   
    )             
''')

def list_all_videos():
    cursor.execute('SELECT * FROM videos')
    rows = cursor.fetchall()
    if not rows:
        print("No videos found in the database.")
    else:
        for row in rows:
            print(row)
            

def add_video(name, time):
    cursor.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (name, time))
    conn.commit()
    
def update_video(video_id, new_name, new_time):
    cursor.execute('UPDATE videos SET name=?, time=? WHERE id=?', ( new_name, new_time, video_id))
    conn.commit()
    
def delete_video(video_id):
    cursor.execute('DELETE FROM videos WHERE id= ?', (video_id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager app with DB | Choose an option ")
        print("1. List all youtube videos: ")
        print("2. Add a youtube video: ")
        print("3. Update a youtube video details: ")
        print("4. Delete a youtube video: ")
        print("5. Exit the app ")
        choice= input("Enter your choice: ")

        # print(videos)

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter video name: ")
                time = input("Enter video length: ")
                add_video(name, time)
            case '3':
                video_id = int(input("Enter the video ID to update: "))
                name = input("Enter new video name: ")
                time = input("Enter new video length: ")
                update_video(video_id, name, time)
            case '4':
                video_id = int(input("Enter the video ID to update: "))
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid Choice")

    conn.close()
if __name__ == "__main__":
    main()