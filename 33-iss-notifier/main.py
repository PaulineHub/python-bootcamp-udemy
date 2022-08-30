import requests
from datetime import datetime
import time

# Montreal position
MY_LAT = 45.5016889
MY_LONG = -73.567256

# to get a response to a request
response = requests.get(url="http://api.open-notify.org/iss-now.json")
#print(response) return <Response [200]>

# to raise an exception :
response.raise_for_status()

data = response.json()
#print(data) return {'message': 'success', 'iss_position': {'longitude': '34.4886', 'latitude': '-49.6808'}, 'timestamp': 1661866514}

iss_longitude = float(data['iss_position']['longitude'])
iss_latitude = float(data['iss_position']['latitude'])
iss_position = (iss_longitude, iss_latitude)


def is_iss_overhead():
    if iss_latitude <= (MY_LAT + 5) and iss_latitude > (MY_LAT - 5) and iss_longitude <= (MY_LONG + 5) and iss_longitude > (MY_LONG - 5):
        return True

# ------------------------------------------------------------
# Sunrise Sunset API

def is_night() :
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data_sun = response_sun.json()

    sunrise = data_sun["results"]["sunrise"]
    sunset = data_sun["results"]["sunset"]
    #print(sunrise) return 2022-08-30T10:12:02+00:00
    #print(sunrise.split("T")) return ['2022-08-30', '10:12:02+00:00']
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    #print(sunset_hour)

    time_now = datetime.now()
    hour_now = time_now.hour
    #print(hour_now)

    if hour_now >= sunset_hour or hour_now < sunrise_hour:
        return True

while True:
    #run the code every 60sec
    time.sleep(60)
    if is_iss_overhead() and is_night():
        print('Look up!')

