import requests
import datetime as dt

# One call API 3.0 which is the current verion when I am programming with this It need a paid subscription.
# So I Use 2.5 version one call API

url = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = '75e527f8cba8b370f9540b36449b84ad'
latitude = 22.718670
longitude = 75.855710

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key
}

response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()
if __name__ == '__main__':
    print(data)
