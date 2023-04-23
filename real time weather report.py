import requests,os
from datetime import datetime
user_api = os.environ['current_weather_data']
location = input('enter the city  name:')
# pasted from website:   api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link= requests.get(complete_api_link)
api_data=api_link.json()
if api_data['cod']=='404':
    print('invalid city name {} :please enter valid city name'.format(location))
else:
# write the data you want to display
     tem=((api_data['main']['temp'])-273.15)
     hmd=api_data['main']['humidity']
     spd=api_data['wind']['speed']
     descr=api_data['weather'][0]['description']
     date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
     print('WEATHER STATS OF {} || {}'.format(location.upper(),date_time))
     print('---------------------------------------')
     print('current temperature is: {:.2f} deg C'.format(tem))
     print('current humidity is: {} %'.format(hmd))
     print('current wind speed is: {} kmph'.format(spd))
     print('current weather description is: {}'.format(descr))
     print('---------------------------------------')
