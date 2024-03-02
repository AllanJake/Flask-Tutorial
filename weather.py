from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def GetCurrentWeather(city="Edinburgh"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n *** Get Current Weather Conditions *** \n')

    city = input("\n Please enter a city name: ")

    # Check for empty strings or only spaces
    if not bool(city.strip()):
        city = "Edinburgh"

    weather_data = GetCurrentWeather(city)

    print ("\n")
    pprint(weather_data)