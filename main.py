import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = Your Api_Key
account_sid = Your Acc_Sid
auth_token = Your Auth_Token

weather_params = {
    "lat": 44.494888,
    "lon": 11.342616,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.status_code)
response.raise_for_status()   # This line of code raises an exception if there is any error.
weather_data = response.json()
# print(weather_data)
weather_slice = weather_data["hourly"][:12]
print(weather_slice)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    # print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today, remember to bring an ☂",
        from_="+16693222517",
        to=Your Phone Number
    )
    print(message.status)

    
# print(weather_data["hourly"][0]["weather"][0]["id"]) #This is how to access items inside a nested json.



