import requests
from twilio.rest import Client
# import os
# from twilio.http.http_client import TwilioHttpClient

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
OWM_API_KEY = "874c73b86ba4a0760706aaade08ea234"

TWILIO_ACCOUNT_SID = "ACa2e5c9541d9bc7e55e5eb8f083c85415"
TWILIO_AUTH_TOKEN = "d30eafd2879e0d4b705788a0c6bfcd98"
TWILIO_PHONE_NUMBER = "+16606285102"
MY_PHONE_NUMBER = "+40753640800"

weather_params = {
    "lat": 45.9575384,
    "lon": 23.5691574,
    "appid": OWM_API_KEY
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

if int(weather_data["weather"][0]["id"]) < 700:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(username=TWILIO_ACCOUNT_SID, password=TWILIO_AUTH_TOKEN)  # http_client = proxy_client

    message = client.messages.create(
        body="It's raining today. Remember to bring an ☔️",
        from_=TWILIO_PHONE_NUMBER,
        to=MY_PHONE_NUMBER
    )

    # print(message.status)
