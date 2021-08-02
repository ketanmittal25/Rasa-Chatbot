import requests
import pandas as pd

def weather_func(day):
    url1 = "https://goweather.herokuapp.com/weather/india"

    json_data = requests.get(url1).json()
    today_temp = json_data['temperature'] 
    print(json_data)
    forecast = json_data['forecast']
    print(forecast)

    if(day == "Today" or day == "today"):
        return {'day': 'today', 'temperature' : today_temp}
    elif(day.split(" ")[1]== '1' or day.split(" ")[1] == 1):
        return forecast[0]
    elif(day.split(" ")[1]== '2' or day.split(" ")[1] == 2):
        return forecast[1]
    elif(day.split(" ")[1]== '3' or day.split(" ")[1] == 3):
        return forecast[2]
    else:
        return {'day':'No data', 'temperature': 'No data'}
