"""
This script scrapes the food offered in the Mensa of U Konstanz.
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# Initialize beautifulsoup.
source_code = requests.get('https://www.seezeit.com/essen/speiseplaene/menseria-giessberg/')
soup = BeautifulSoup(source_code.content)

# Get day and date of each tab.
list_of_tabs = ['tab1', 'tab2', 'tab3', 'tab4', 'tab5', 'tab6', 'tab7', 'tab8', 'tab9', 'tab10']
dict_of_tabs = {'tab1': None, 'tab2': None, 'tab3': None, 'tab4': None, 'tab5': None, 'tab6': None, 'tab7': None, 'tab8': None, 'tab9': None, 'tab10': None}

tabs = soup.find('div', {'class': 'tabs'})

for key in dict_of_tabs:
    print(tabs.find_all('a', {'class': key})[0])

    dates = tabs.find('a', {'class': key})
    for span in dates.find_all('span'):
        dict_of_tabs[key] =span.get_text()


for d in dict_of_tabs:
    if dict_of_tabs[d] is not None:
        print(d + ":", dict_of_tabs.get(d))


monday = soup.find('div', {'id': 'tab1'})


for key in dict_of_tabs:
    day = soup.find('div', {'id': key})

    print("-----------------------------------------------------------------")
    print("On", dict_of_tabs.get(key), "the following meals will be served: ")
    speiseplan = day.find_all('div', {'class': 'speiseplanTagKat'})
    for i in speiseplan:
        print("Categ.:\t", i.find('div', {'class': 'category'}).get_text().split(","))
        print("Meal:\t", i.find('div', {'class': 'title'}).get_text().split(", "))
        if i.find('div', {'class': 'preise'}) is not None:
            print("Preise:\t", i.find('div', {'class': 'preise'}).get_text().split("|"))
        else: print("Preise:\t - ")
        print(" ")
    print(" ")



tuesday = soup.find('div', {'id': 'tab2'})

children = monday.findChildren()
for child in children:
    print("--------------------------")
    if child.find()

tables = soup.find_all('table')
