import sqlite3
connection=sqlite3.connect("contact_book.db")
cursor=connection.cursor()
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS contact(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL,
phone TEXT NOT NULL,
address TEXT NOT NULL
        )
    """)
connection.commit()

def list_all_the_data():
    cursor.execute("SELECT * FROM contact")
    for i in cursor.fetchall():
        print(i)

    

def add_the_data():
    list_all_the_data()
    name=input("Enter name ")
    phone=input("Enter phone ")
    email=input("Enter email ")
    address=input("Enter address ")
    cursor.execute("INSERT INTO contact (name,email,address,phone) values(?,?,?,?)",(name,email,address,phone))
    connection.commit()
    
    
def update_the_data():
     list_all_the_data()
     
     id=int(input("Enter the video id you have to update "))
     new_name=input("Enter the name to update ")
     new_email=input("Enter the email to update ")
     new_address=input("Enter the address to update ")
     new_phone=input("Enter the phone to update ")
     cursor.execute("UPDATE contact SET name=?,email=?,address=?,phone=? WHERE id=?",(new_name,new_email,new_address,new_phone,id))
     connection.commit()
     
     
def delete_the_data():
     list_all_the_data()
     id=int(input("Enter the video id you have to delete "))
     cursor.execute("DELETE FROM contact WHERE id=?",(id,))
     connection.commit()
     

def main():
    
    while True:
        print("\n Welcome to contact book");
        print("1. list all the contacts ")
        print("2. add the contact ")
        print("3. update the contact ")
        print("4. delete the contact ")
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