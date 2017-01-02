"""
This script scrapes the 'Importance of Religion' table from wikipedia.
The original data is from gallup but is not accessible anymore.
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

source_code = requests.get('https://en.m.wikipedia.org/wiki/Importance_of_religion_by_country')
soup = BeautifulSoup(source_code.content)
religiondatasaved=""
tables = soup.find_all('table', class_="wikitable")

table = tables[0]

for record in table.findAll('tr'):
    religiondata=""
    for data in record.findAll('td'):
        religiondata = religiondata + "," + data.text
        print(religiondata)
    religiondatasaved = religiondatasaved + "\n" + religiondata[1:]


