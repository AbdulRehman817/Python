import sqlite3

connection=sqlite3.connect("youtube_videos.db")
cursor=connection.cursor()
cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS videos(
                id  INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
            )   
     ''');
connection.commit()

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def  add_video():
    name=input("Enter video name")
    time=input("Enter video time")
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    connection.commit()
    
def update_videos():
     list_videos()
     video_id=int(input("Enter video id to update"))
     new_name=input("Enter video name to update")
     new_time=input("Enter video time to update")
     cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(new_name,new_time,video_id))
     connection.commit()

def delete_videos():
    list_videos()
    video_id=int(input("Enter video id to delete"))
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
    connection.commit()
    
def main():
    while True:
        print("\n Youtube Manager with db")
        print("1. list videos")
        print("2. add videos")
        print("3. update videos")
        print("4. delete videos")
        print("4. exist")
        choice=input("Enter your choice")
        
        match choice:
            case "1":
                list_videos()
            case "2":
                
                add_video()
            case "3":
               
                update_videos()
            case "4":
                
                delete_videos()
            case "5":
                break;
    connection.close()

if __name__ == "__main__":
    main()