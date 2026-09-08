# import requests

# with open("json/preview.json", "w", encoding="UTF-8") as f:
#     r = requests.get("https://api.open-meteo.com/v1/forecast", params={
#                 "latitude": 55.75,
#                 "longitude": 37.61,
#                 # "hourly": "temperature_2m"
#                 # "current": "temperature_2m"
#                 "hourly": ["temperature_2m", "precipitation_probability"],
#                 "current": ["temperature_2m", "apparent_temperature", "is_day", "rain,wind_speed_10m"]
#                 })
#     f.write(r.text)

# # r = requests.get("https://api.open-meteo.com/v1/forecast", params={
# #                 "latitude": 55.75,
# #                 "longitude": 37.61,
# #                 # "hourly": "temperature_2m"
# #                 # "current": "temperature_2m"
# #                 "hourly": ["temperature_2m", "precipitation_probability"],
# #                 "current": ["temperature_2m", "apparent_temperature", "is_day", "rain,wind_speed_10m"]
# #                 })

# # current=temperature_2m,apparent_temperature,is_day,rain,wind_speed_10m
# # hourly=temperature_2m,precipitation_probability
# # print(r.json())

print(55.34234%10)