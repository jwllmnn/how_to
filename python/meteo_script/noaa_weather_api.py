"""
This script takes a lat/long coordinate and a date and returns the weather (specifically, whether it rained or not)
for the given day.
"""

import requests
import json


def get_noaa_weather(lat, long, date, token):
    headers = {'token': token}

    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND'
    url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes'

    response = requests.get(url, headers=headers)
    response = response.json()
    response

