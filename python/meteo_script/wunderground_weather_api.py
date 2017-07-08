"""
This script takes a lat/long coordinate and a date and returns the weather (specifically, whether it rained or not)
for the given day.
"""

import requests


def get_underground_weather(lat, long, date, key):
    """
    Function to retrieve historical weather data for given location and date.
     Uses 'Weather Underground API'.
    :param lat: Latitude.
    :param long: Longitude.
    :param date: Date to be retrieved (YYYYMMDD).
    :param key: API key; need account for 'https://www.wunderground.com'.
    :return:
    """
    response = requests.get("http://api.wunderground.com/api/" + key + "/history_" + str(date) + "/q/" + str(lat) + "," + str(long) +".json")
    response = response.json()

    rain = response['history']['dailysummary'][0]['rain']  # Binary indicator whether it rained or not (1 or 0).
    precipm = response['history']['dailysummary'][0]['precipm']  # Amount of precipitation (metric system).
    maxtempm = response['history']['dailysummary'][0]['maxtempm']  # Max. Temperature of day (°C).
    meantempm = response['history']['dailysummary'][0]['meantempm']  # Mean Temperature of day (°C).
    mintempm = response['history']['dailysummary'][0]['mintempm']  # Min. Temperature of day (°C).
    meanwindspdm = response['history']['dailysummary'][0]['meanwindspdm']  # Mean wind speed (metric system).

    return rain, precipm, maxtempm, meantempm, mintempm, meanwindspdm





