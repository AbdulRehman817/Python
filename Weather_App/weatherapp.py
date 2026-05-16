from datetime import date
import requests
import sqlite3
connection=sqlite3.connect("weather.db")
cursor=connection.cursor()
cursor.execute(""" 
               CREATE TABLE IF NOT EXISTS weather_app(
               id INTEGER PRIMARY KEY,
               city_name TEXT NOT NULL,
               country TEXT NOT NULL,
               temperature REAL NOT NULL,
               condition TEXT NOT NULL,
               searched_at TEXT NOT NULL
               )
               """)
connection.commit()


def search_weather():
    inp=input("Enter city name ")
    # cursor.execute("INSERT INTO weather_app (city_name) values(?)",inp,)
    url=f"https://api.openweathermap.org/data/2.5/weather?q={inp}&appid=89cdf543f0a247ecb3c5697f04de1139&units=metric?"
    response=requests.get(url)
    data=response.json()
    if "main" in data and "weather" in data:
            searched_at=date.today().isoformat()
            city_name=data['name']
            country=data['sys']['country']
            temperature=data['main']['temp']
            condition=data['weather'][0]['description']
            cursor.execute("INSERT INTO weather_app (city_name,country,temperature,condition,searched_at) VALUES(?,?,?,?,?)",(city_name,country,temperature,condition,searched_at))
            connection.commit()
            return city_name,country,temperature,condition
    else:
        raise Exception("Failed to fetch data")
        
def forecast():
    forecast_list=[]
    inp=input("Enter city name ")
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={inp}&appid=89cdf543f0a247ecb3c5697f04de1139&units=metric"
    response=requests.get(url)
    data=response.json()
    
    city_name = data['city']['name']              # city name from forecast response
    country   = data['city']['country'] 
    entries=data['list']
    for i in entries:
        text=i['dt_txt']
        split=text.split(" ")
        date_1=split[0]
        time=split[1]
        if time=="12:00:00":
            
            temperature=i['main']['temp']
            feels_like  = i['main']['feels_like']         # feels like temp
            humidity    = i['main']['humidity']           # humidity %
            wind_speed  = i['wind']['speed']  
            condition=i['weather'][0]['description']
            day_data={
                "date":date_1,
                "temperature":temperature,
                "feels_like":feels_like,
                "humidity":humidity,
                "wind_speed":wind_speed,
                "condition":condition                
            }
            forecast_list.append(day_data)
            
        else:
            continue
# match the unpacking order: city_name, country, forecast_list
    return city_name, country, forecast_list                        

def view_history():
    
    cursor.execute("SELECT city_name, country, temperature, condition, searched_at FROM weather_app ")
    rows=cursor.fetchall()
    if not rows:
        print("no search history found")
        return
    else:
            print("\n" + "=" * 45)
    print("           SEARCH HISTORY")
    print("=" * 45)
 
    for index, row in enumerate(1):         # loop through rows
        print(f"\n  Search {index}")
        print(f"  City        : {row[0]}, {row[1]}")
        print(f"  Temperature : {row[2]}°C")
        print(f"  Condition   : {row[3]}")
        print(f"  Searched At : {row[4]}")
        print("  " + "-" * 40)
 
    print("=" * 45)
    
def delete_history():
    user_inp=input("Are you sure you want to delete search history ").lower()
    if user_inp == "yes":
        cursor.execute("DELETE FROM weather_app")
        connection.commit()
    else:
        print("History not cleared")
        return

        
        
    
    
def main():
    while True:
        print("\n === Welcome to Weather App ===")
        print("1. Search Weather")
        print("2. View 5-Day Forecast")
        print("3. Search History ")
        print("4. Delete History ")
        print("5. Exit ")
        choice=input("Enter the number to perform action accordingly ")
        match choice:
            case "1":
                city_name,country,temperature,condition=search_weather()
                print("City ",city_name)
                print("country ",country)
                print("temperature ",temperature)
                print("condition",condition)
            case "2":
                city_name,country,forecast_list=forecast()
                 
                print("=" * 45)
                print(f"   5-Day Forecast for {city_name}, {country}")
                print("=" * 45)
            
                for index, day in enumerate(forecast_list, 1):   # loop through 5 entries
                    print(f"\n  Day {index}  →  {day['date']}")
                    print(f"  Temperature  : {day['temperature']}°C")
                    print(f"  Feels Like   : {day['feels_like']}°C")
                    print(f"  Condition    : {day['condition']}")
                    print(f"  Humidity     : {day['humidity']}%")
                    print(f"  Wind Speed   : {day['wind_speed']} m/s")
                    print("  " + "-" * 40)
            
                print("=" * 45)
                    
            case "3":
                view_history()    
            case "4":
                delete_history()
            case "5":
                    break;
                    
    
if __name__=="__main__":
    main()