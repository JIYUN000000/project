import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "{API-KEY}"
account_sid = "{ACCOUNT_SID}"
auth_token = "{AUTH_TOKEN}"

weather_params = {
    "lat": 35.58,
    "lon": 94.7,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}
response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 900:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="Active number",
        to="My phone number",
    )
    print(message.status)
