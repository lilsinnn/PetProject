from get_weather import get_weather
import time

def generate(data: dict, mode: int):
    """
    Makes smth like beatiful answer
    """ 

    if data["current"]["is_day"] == 1:
        is_day = "День"
    else:
        is_day = "Ночь"

    if mode == 1:
        
        print(
        f"Страна: {data['country']}\n"
        f"|\tТемпература: {data['current']['temperature_2m']}{data['current_units']['temperature_2m']}\n"
        f"|\tОщущается как: {data['current']['apparent_temperature']}{data['current_units']['apparent_temperature']}\n"
        f"|\tСкорость ветра: {data['current']['wind_speed_10m']}{data['current_units']['wind_speed_10m']}\n"
        f"|\t{is_day}\n"
        f"----------------------------------"
    )
    if mode == 2:
        ##
        # day = 24
        # print(
        # f"Страна: {data['country']}\n"
        # f"Осадки и погода на ближайшие 24 часа:\n")
        # for i in data["hourly"]:
        #     day += 1
        #     if day == 24:
        #         break
        #     date = i["time"][:5]
        #     temperature = i["temperature_2m"]
        #     precipitation = i["precipitation_probability"]
        #     print(f"\t{date}| {temperature}{data['hourly_units']['temperature_2m']} {precipitation}{data['hourly_units']["precipitation_probability"]}")
        hourly = data["hourly"]

        print(
                f"Страна: {data['country']}\n"
                f"Осадки и погода на ближайшие 24 часа:\n")

        # current_time = time.strftime("%H:%M")

        # start_time = current_time[0] + current_time[1] # 12 maybe here can be error with time lower than 11
        current_time = int(time.strftime("%H"))
        try:
            for i in range(current_time, 25 + current_time):
                        date = hourly["time"][i][11:]
                        temperature = hourly["temperature_2m"][i]
                        precipitation = hourly["precipitation_probability"][i]
                        print(f"\t{date} | {temperature}{data['hourly_units']['temperature_2m']} {precipitation}{data['hourly_units']["precipitation_probability"]}")
        except Exception as e:
            print(f"Something went wrong: {e}")

    

        

