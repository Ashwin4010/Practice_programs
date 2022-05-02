import requests
from twilio.rest import Client
import os

account_sid = "ACeac340b685febbef7b7cdce975c2f084"
auth_token = os.environ.get("AUTH_TOKEN")


api_key = os.environ.get("OWM_API_KEY")
print(api_key)
OWM_Endpoint ="https://api.openweathermap.org/data/2.5/onecall?"

PARAMETERS = {
    "lat": 40.440624,
    "lon": -79.995888,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
weather_slice = weather_data["hourly"][:12]

will_rain = False
print(weather_slice)
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Probably Gonna Rain tomorrow, so bring an Umbrella. ☂ ",
        from_='+16098495613',
        to='+919952062092'
    )
    print(message.status)
