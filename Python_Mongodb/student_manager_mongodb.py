from bson import ObjectId
from datetime import date
from pymongo import MongoClient
try:
    client=MongoClient("mongodb+srv://abdulrehmanbey2007_db_user:abdulrehmanbey2007@cluster0.eamiwm4.mongodb.net/")
    db=client['student_manager']
    student_manager_collection=db["students"]
except Exception as e:
    print(str(e))

def list_all_the_data():
   for students in student_manager_collection.find():
       print("id",students['_id'],"name:",students['name'],"age:",students['age'],"email:",students['email'],"course:",students['course'],"grade:",students['grade'])
    
def add_the_data():
    list_all_the_data()
    name=input("Enter name ")
    age=input("Enter age ")
    email=input("Enter email ")
    course=input("Enter course ")
    grade=input("Enter grade ")
    today = date.today().isoformat()
    student_manager_collection.insert_one({"name":name,"age":age,"email":email,"course":course,"grade":grade,"enrolled_on":today})
    
    
def update_the_data():
    list_all_the_data()
    id=input("Enter id to update ")
    new_name=input("Enter name ")
    new_age=input("Enter age ")
    new_email=input("Enter email ")
    new_course=input("Enter course ")
    new_grade=input("Enter grade ")
    student_manager_collection.update_one({"_id":ObjectId(id)},
                                          {"$set":{"name":new_name,"age":new_age,"email":new_email,"course":new_course,"grade":new_grade}}
                                          )  #TODO: if we donot add objectid then it will create new document instead of updating the existing one because mongodb will not be able to find the document with the given id and it will create new document with the given id as a field and it will not update the existing

    
def delete_the_data():
    list_all_the_data()
    id=input("Enter id to delete ")
    student_manager_collection.delete_one({"_id":ObjectId(id)})
    

def main():
    try:
    
        while True:
            print("\n Welcome to Student Manager");
            print("1. list all the student's information ")
            print("2. add the student ")
            print("3. update the student info ")
            print("4. delete the student info ")
            print("5. exit the app")
            choice=input("Enter the number to perform action accordingly ")
            match choice:
                case "1":
                    list_all_the_data();
                case "2":
                    add_the_data();
                case "3":
                    update_the_data();
                case "4":
                    delete_the_data();
                case "5":
                    break
                case _:
                    print("Invalid number")
    except Exception as e:
                print(str(e))
        
if __name__ == "__main__":
    main()