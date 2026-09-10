import requests
from generate_output import generate
from get_weather import get_weather
from get_geo import geo


# def main():
#     city = input("Enter city: ")
#     generate(get_whether(geo(city)))
#     input()

def main():
    mode = int(input(f"1 - current\n2 - hourly"))
    city = input("Enter city: ")
    if mode == 1:
        generate(get_weather(geo(city)), 1)
        input()
    elif mode == 2:
        generate(get_weather(geo(city)), 2)
        input()
    else:
        print("only 1 or 2")

while True:
    try:
        main()
    except KeyError:
        print("\nError")
    except KeyboardInterrupt:
        print("\nBye")
        break
    except ValueError:
        print("choose one of modes")
        continue
