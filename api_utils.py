# import requests
# import pandas as pd
# resp = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=12.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m')
# print(resp.status_code)
# data = resp.json()
# print(type(data))
# print(data.keys())
# print(data['current_weather'].keys())
# print(data['current_weather']['temperature'])
# print(data['hourly'].keys())
# print(len(data['hourly']['time']))
# #print(data['hourly']['time'])
# # ['time', 'temperature_2m', 'relativehumidity_2m', 'windspeed_10m']
# hourly_data = pd.DataFrame(data['hourly'])
# print(hourly_data)
# hourly_data['city'] = 'india'
# print(hourly_data)

for i in range(10):
    url = i
print(url)
