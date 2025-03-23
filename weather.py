import requests

city_name='Madhya Pradesh'
API_key='63833b057ef78e234b5abca7c2028418'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metrics'


response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print('weather is',data['weather'][0]['description'])
    print('Current Temperature is',data['main']['temp'])
    print('Current Temperature Feels like is',data['main']['feels_like'])
    print('Current humidity is',data['main']['humidity'])
else:
    print('Error:', response.status_code, response.json().get("message", "Invalid request"))