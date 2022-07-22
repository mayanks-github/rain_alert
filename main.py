import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

# One call API 3.0 which is the current verion when I am programming with this It need a paid subscription.
# So I Use 2.5 version one call API

load_dotenv()

weather_url = os.getenv('WEATHER_URL')
api_key = os.getenv('API_KEY')
latitude = 22.718670
longitude = 75.855710

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
phone_number = os.getenv('PHONE_NUMBER')
client_number = os.getenv('CLIENT_NUMBER')
client = Client(account_sid, auth_token)

weather_parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=weather_url, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][:19]

for time in hourly_data:
    weather_id = time["weather"][0]["id"]

    if 531 >= weather_id <= 500:
        message = client.messages \
            .create(
                body="Its going to rain dont forget to bring umbrella ☔",
                from_=phone_number,
                to=client_number
        )
        break
