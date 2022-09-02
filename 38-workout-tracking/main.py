import requests
from datetime import datetime
import os

# ----------------------------------------
# Request POST to Nutritionix API

## Set environment variables in terminal
# export NUTRITIONIX_APP_ID=3851310d
# export NUTRITIONIX_API_KEY=b77b19353568b36576ce53a1a2d50528

## Get environment variables
APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_input = input("Tell me whitch exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

workout_params = {
    "query": user_input,
    "gender": "female",
    "weight_kg": 51,
    "height_cm": 171,
    "age": 30
}

nutritionix_response = requests.post(url=nutritionix_endpoint, json=workout_params, headers=headers)
nutritionix_response.raise_for_status()
workout_data_json = nutritionix_response.json()
workout_data = workout_data_json['exercises'][0]

exercise = workout_data['user_input']
duration = workout_data['duration_min']
calories = workout_data['nf_calories']

# ----------------------------------------------------------------
# Request POST to Sheety

now = datetime.today()
today = now.strftime("%d/%m/%Y")
hour_now = now.strftime("%H:%M:%S")

## Set environment variables in terminal
# export SHEET_ENDPOINT=https://api.sheety.co/e48719e271baa951b0cb14def6302630/myWorkouts/workouts
# export SHEET_TOKEN=f438iyth9hf84hrwry483

## Get environment variables
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
SHEET_TOKEN = os.environ.get("SHEET_TOKEN")

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEET_TOKEN}"
}

sheety_params = {
    "workout": {
        "date": today,
        "time": hour_now,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

sheety_response = requests.post(
    url=SHEET_ENDPOINT, json=sheety_params, headers=sheety_headers)
sheety_response.raise_for_status()
print(sheety_response)
