import requests

url = "https://geocoding-api.open-meteo.com/v1/search"

def geo(city: str): 
    """
    Returns the dict, like
    {
    "latitude": 55.75204,
    "longitude": 37.61781,
    "country": "RU"
    }
    """
    try:
        response = requests.get(url, params={"name": city})
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"API sent error: {e}")
    city_data = response.json()["results"][0]
    city_dict = {}
    city_dict.update({
        "latitude": city_data["latitude"],
        "longitude": city_data["longitude"],
        "country": city_data["country"]
    })
    return city_dict



