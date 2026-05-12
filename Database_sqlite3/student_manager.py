from datetime import date
import sqlite3
connection=sqlite3.connect("student_manager.db")
cursor=connection.cursor()
cursor.execute('''  
               CREATE TABLE IF NOT EXISTS student_manager(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               age TEXT NOT NULL,
               email TEXT NOT NULL,
               course TEXT NOT NULL,
               grade TEXT NOT NULL,
               enrolled_on TEXT NOT NULL
               )
               ''')
connection.commit()
def list_all_the_data():
    cursor.execute("SELECT * FROM  student_manager")
    for i in cursor.fetchall():
        print(i)
    connection.commit()
    
def add_the_data():
    list_all_the_data()
    name=input("Enter name ")
    age=input("Enter age ")
    email=input("Enter email ")
    course=input("Enter course ")
    grade=input("Enter grade ")
    today = date.today().isoformat()
    cursor.execute("INSERT INTO student_manager (name,age,email,course,grade,enrolled_on) VALUES(?,?,?,?,?,?)",(name,age,email,course,grade,today))
    connection.commit()
    
    
def update_the_data():
    list_all_the_data()
    id=int(input("Enter id to update "))
    new_name=input("Enter name ")
    new_age=input("Enter age ")
    new_email=input("Enter email ")
    new_course=input("Enter course ")
    new_grade=input("Enter grade ")
    cursor.execute("UPDATE student_manager SET name=?,age=?,email=?,course=?,grade=? WHERE id=?",(new_name,new_age,new_email,new_course,new_grade,id))
    connection.commit()
    
    
def delete_the_data():
    list_all_the_data()
    id=int(input("Enter id to update "))
    cursor.execute("DELETE FROM student_manager WHERE id=?",(id,))
    connection.commit()
    

def main():
    
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
        
if __name__ == "__main__":
    main()