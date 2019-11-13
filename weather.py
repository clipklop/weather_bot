"""
    * Gets Weather forecast by city's name
"""

from settings import WEATHER_API
import requests


def temperature(city):
    response = requests.get("".format(city, WEATHER_API))
    return response
    # not finished yet
