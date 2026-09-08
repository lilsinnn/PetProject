import requests
from generate_output import generate
from get_whether import get_whether
from get_geo import geo


def main():
    city = input("Enter city ")
    generate(get_whether(geo(city)))
    input()

while True:
    main()
