from bson.objectid import ObjectId
from pymongo import MongoClient
client=MongoClient("mongodb+srv://abdulrehmanbey2007_db_user:abdulrehmanbey2007@cluster0.eamiwm4.mongodb.net/")
db=client['ytmanager']
video_collection=db['videos']
print(video_collection)


def list_videos():
    for video in video_collection.find():
        print(f"id: {video['_id']}, Name: {video["name"]}, Time: {video["time"]}")
        
def add_video():
    name=input("Enter video name ")
    time=input("Enter video time ")
    video_collection.insert_one({"name":name,"time":time})
    
    
def update_videos():
    video_id=input("Enter video id to update ")
    new_name=input("Enter video name to update ")
    new_time=input("Enter video time to update ")
    video_collection.update_one({'_id':ObjectId(video_id)},{"$set":{"name":new_name,"time":new_time}})

def delete_videos():
    video_id=input("Enter video id to delete ")
    video_collection.delete_one({'_id':ObjectId(video_id)})

def main():
    while True:
        print("\n Youtube Manager with db")
        print("1. list videos")
        print("2. add videos")
        print("3. update videos")
        print("4. delete videos")
        print("5. exist")
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
        

if __name__=="__main__":
    main()