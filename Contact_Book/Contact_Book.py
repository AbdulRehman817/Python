import json
def load_data():
    try:
        with open("contacts.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(contacts):
    with open("contacts.txt",'w') as file:
        return json.dump(contacts,file)
        

def list_all_the_data(contacts):
  for index,contact in enumerate(contacts,start=1):
      print(f'{index }. name={contact['name']} , email={contact['email']} , address={contact['address']} , contact={contact['phone']}' )
    
def add_the_data(contacts):
    name=input("Enter name ")
    phone=input("Enter phone ")
    email=input("Enter email ")
    address=input("Enter address ")
    contacts.append({"name":name, "phone":phone, "email":email, "address":address})
    save_data_helper(contacts)


def update_the_data(contacts):
    list_all_the_data(contacts)
    index=int(input("Enter the video number you have to update "))
    
    if 1<=index<=len(contacts):
        name=input("Enter the name to update ")
        email=input("Enter the email to update ")
        address=input("Enter the address to update ")
        phone=input("Enter the phone to update ")
        contacts[index-1]={"name":name, "phone":phone, "email":email, "address":address}
    save_data_helper(contacts)

def delete_the_data(contacts):
    list_all_the_data(contacts)
    index=int(input("Enter the video number you have to delete"))
    if 1<=index<=len(contacts):
        del contacts[index-1]
    save_data_helper(contacts)


def main():
    contacts=load_data()
    while True:
        print("\n Welcome to contact book");
        print("1. list all the contacts ")
        print("2. add the contact ")
        print("3. update the contact ")
        print("4. delete the contact ")
        print("5. exit the app")
        choice=input("Enter the number to perform action accordingly")
        match choice:
            case "1":
                list_all_the_data(contacts);
            case "2":
                 add_the_data(contacts);
            case "3":
                 update_the_data(contacts);
            case "4":
                 delete_the_data(contacts);
            case "5":
                 break
            case _:
                 print("Invalid number")
        
if __name__ == "__main__":
    main()
    