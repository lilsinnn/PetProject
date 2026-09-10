import requests
from get_geo import geo

def get_weather(geo: dict):
    """
    Gets dict from get_geo.py and finds whether for those coords
    """
    try:
        whether_json = requests.get("https://api.open-meteo.com/v1/forecast", params={
                        "latitude": geo["latitude"],
                        "longitude": geo["longitude"],
                        "hourly": ["temperature_2m", "precipitation_probability"],
                        "current": ["temperature_2m", "apparent_temperature", "is_day", "rain", "wind_speed_10m"]
        })
        whether_json.raise_for_status()
    except requests.RequestException as e:
        print(f"API sent error: {e}")

    # print(whether_json.json())
    whether = whether_json.json()
    whether["country"] = geo["country"]
    return whether

# with open("tmp.json", "w", encoding="UTF-8") as f:
#     f.write(str(get_whether(data("Moscow"))))