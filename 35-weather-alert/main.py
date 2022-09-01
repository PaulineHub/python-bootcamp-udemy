import requests
import os # to import env variable

# to export a variable in our local environment
# enter in terminal : 
# export WEATHER_API_KEY=xxxxx (our key)
# to check local environement, enter in terminal : env

# Montreal position
MY_LAT = 45.5016889
MY_LONG = -73.567256

# to import the api key of our online account, registered in our local environment
API_KEY = os.environ.get("WEATHER_API_KEY")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY
}

# to get a response to a request
response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
# to raise an exception :
response.raise_for_status()
weather_data = response.json()
weather_id = weather_data['weather'][0]['id']
will_rain = False
print(weather_id)

# 2xx : Thunderstorm
# 3xx : Drizzle
# 5xx : Rain
if weather_id >= 200 and weather_id < 532:
    will_rain = True

if will_rain:
    print("Bring an umbrella.")




