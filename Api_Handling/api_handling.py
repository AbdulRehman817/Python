# import requests

# def fetch_random_users():
#     url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
#     response=requests.get(url)
#     data=response.json()
#     if data["success"] and "data" in data:
#        user_data=data['data']
#        username=user_data["login"]["username"]
#        country=user_data["location"]["country"]
#        return username , country
#     else:
#        raise Exception("Fail to fetch user data")
      
      
# def main():
#     try:
#         username,country=fetch_random_users()
#         print(f"username {username} \n country {country}")
#     except Exception as e:
#         print(str(e)) 
        

# if __name__ == "__main__":
#     main()
    
    
import requests
def get_jokes():
    url = 'https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%252Cid%252Ccontent&page=1';
    response=requests.get(url)
    data=response.json() 
    
    if data['success'] and "data" in data:
        jokes=data['data']['data']
        return jokes
    else:
        raise Exception("Error coming while fetching jokes")
    
    
    
    
def add_jokes():
    url = 'https://api.freeapi.app/api/v1/public/randomjokes';
    new_joke={"categories":["science"],"content":"new science joke"}
    response=requests.post(url,json=new_joke)
    print("new joke added",response.json())
    

def update_jokes(joke_id):
    url = f'https://api.freeapi.app/api/v1/public/randomjokes/{joke_id}';
    
    updated_joke={"content":"updated science joke"}
    response=requests.put(url,json=updated_joke)
    print("new joke updated",response.json())
    
def delete_jokes(joke_id):
    url = f'https://api.freeapi.app/api/v1/public/randomjokes/{joke_id}';
    response=requests.delete(url)
    print("joke deleted",response.json())
    
def main():
    try:
        jokes=get_jokes()
        for i in jokes:
            print(i["content"])
        add_jokes()
        update_jokes(140)
        delete_jokes(140)
    except Exception as e:
        print(str(e))
        
   
        
if __name__=="__main__":
    main()

    


