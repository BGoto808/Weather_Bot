#########################################################
# Weather_api.py: Program that allows the user to input
#    a city and obtains the current weather of that city
#
# Author: Bryson Goto, 2/10/2022
# 
#########################################################

# Importing libraries
import requests, json

# Base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# User inputs a city
CITY = input("Enter a city: ")

# API key for WeatherMap
API_KEY = "9fe048215c91d6c4f2f280b4e0b8cb5c"

# Updating the URL to connect to
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

# HTTP request
response = requests.get(URL)

# Checking the status code of the request
if response.status_code == 200:
   # Formatting data into json
   data = response.json()

   # Getting main dictionary
   main = data['main']

   # Getting temperature and converting from Kelvin to Fahrenheit
   temperature = main['temp']
   temperature = int(temperature * 1.8 - 459.67)

   # Getting the humidity
   humidity = main['humidity']

   # Getting the pressure
   pressure = main['pressure']

   # Printing weather information
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:
   # Prints error message
   print("Error in the HTTP request")