#!/usr/bin/env python
# coding: utf-8

# In[25]:


import requests
import json
from pprint import pprint


# In[26]:


api_key = "Enter API Key here from OpenWeatherMap"
lat = input("please enter latitude")
#"35.776"
lon = input("please enter longitude")
#"-78.6382"
exclude = "minutely,hourly,alerts"
units = "imperial"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=%s&appid=%s&unit=%s" %(lat,lon, exclude, api_key,units)
response = requests.get(url)
weather_response = json.loads(response.text)
pprint(weather_response)


# In[27]:


daily_array = weather_response["daily"]
pprint(daily_array)


# In[28]:


def weather():
    """
    create dictionary
    create variables that will serve as keys for humidity,temperature,current time,windspeed,weather
    add keys and value to dictionary and return list
    """
    weather_list = []
    
    for weather_dictionary in daily_array:
  
        weather_dictionary_print = {}
       
        humidity = weather_dictionary["humidity"]
        temperature = weather_dictionary["temp"]
        current_time = weather_dictionary["dt"]
        windspeed = weather_dictionary["wind_speed"]
        weather = weather_dictionary["weather"]
    
        weather_dictionary_print["humidity"]=humidity
        weather_dictionary_print["temp"]=temperature
        weather_dictionary_print["dt"]=current_time
        weather_dictionary_print["windspeed"]=windspeed
        weather_dictionary_print["weather"] = weather
   
        weather_list.append(weather_dictionary_print)
    return(weather_list)

seven_day_forecast = weather()
pprint(seven_day_forecast)


# In[29]:


def format_weather_list(seven_day_forecast):
    """
    extract desired items and print out in clear format
    """
    for item in seven_day_forecast:
        print("-----------------------------------")
        pprint("current time: " + str(item["dt"]))
        temperature = item["temp"]
        pprint("evening temperature: " + str(temperature["eve"]))
        
        main_weather_list = item["weather"]
        main_weather_dictionary = main_weather_list[0]
        pprint("current weather: " + (main_weather_dictionary["main"]))
        pprint("humidity: " + str(item["humidity"]))
        pprint("windspeed: " + str(item["windspeed"]))
        
format_weather_list(seven_day_forecast)


# In[ ]:




