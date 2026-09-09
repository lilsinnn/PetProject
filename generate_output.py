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
    f"Страна: {data['country']}\n"
    f"|\tТемпература: {data['current']['temperature_2m']}{data['current_units']['temperature_2m']}\n"
    f"|\tОщущается как: {data['current']['apparent_temperature']}{data['current_units']['apparent_temperature']}\n"
    f"|\tСкорость ветра: {data['current']['wind_speed_10m']}{data['current_units']['wind_speed_10m']}\n"
    f"|\t{is_day}\n"
    f"----------------------------------"
)


