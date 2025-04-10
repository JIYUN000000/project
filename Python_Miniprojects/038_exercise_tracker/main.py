import requests
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()

GENDER = "female"
WEIGHT_KG = 50
HEIGHT_CM = 163
AGE = 25

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv('SHEET_ENDPOINT')

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

add_params = {
    "email": {
        "name": "Jiyun K",
        "email": "brilliantstar120@gmail.com"
    }
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise['user_input'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, auth=(os.getenv('SHEETY_USERNAME'), os.getenv('SHEETY_PASSWORD')))
    print(sheet_response.text)
