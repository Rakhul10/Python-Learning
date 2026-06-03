
import requests
from dotenv import load_dotenv
import os
from pprint import pprint
load_dotenv()
def get_weather():
    print('\n*** Get current weather conditions***\n')
    city = input('Enter the city name: ')   
    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=imperial'
    #print(request_url)
    weather_data = requests.get(request_url).json()
    #pprint(weather_data)
    print(f"\nCurrent temperature in {city} is {weather_data['main']['temp']}°F")
if __name__ == "__main__":
        get_weather()

