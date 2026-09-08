from get_whether import get_whether

def generate(data: dict):
    """
    Makes smth like beatiful answer
    """ 
    important_info_dict = {}
    if data["current"]["is_day"] == 1:
        is_day = "День"
    else:
        is_day = "Ночь"
    print(
    f"Город: {data['country']}\n"
    f"Температура: {data['current']['temperature_2m']}{data['current_units']['temperature_2m']}\n"
    f"Ощущается как: {data['current']['apparent_temperature']}{data['current_units']['apparent_temperature']}\n"
    f"Скорость ветра: {data['current']['wind_speed_10m']}{data['current_units']['wind_speed_10m']}\n"
    f"{is_day}"
)


