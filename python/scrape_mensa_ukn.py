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

# title.
title = monday.find('div', {'class': 'title'}).get_text()

for t in monday.find_all('div', {'class': 'title'}):
    title_clean = re.sub(' +', ' ', re.sub(r'\([^)]*\)', '', t.get_text()))
    print(title_clean)
    price = re.search(r'(100g /)* \d,\d\d Euro', title_clean)
    title_exclude_price = re.sub(r'(100g /)* \d,\d\d Euro', '',title_clean)
    print(title_exclude_price)
    if price is not None:
        print("Price:", price.group(0))
    else:
        print("Price: None")

    title_list = [x.strip() for x in re.split(', | und ', title_clean)]




title_clean = re.sub(' +',' ', re.sub(r'\([^)]*\)','', title))
title_list = [x.strip() for x in re.split(', | und ',title_clean)]

# category.
cat = monday.find('div', {'class': 'category'}).get_text()
cat_clean = re.sub(' +',' ', re.sub(r'\([^)]*\)','', cat))


print("Preise:\t", monday.find('div', {'class': 'preise'}).get_text().split("|"))

# price.
if monday.find('div', {'class': 'preise'}) is not None:
    price = re.sub(' +',' ', monday.find('div', {'class': 'preise'}).get_text()).split(" | ")
    for p in price:
        if "Studierende" in p:
            student_price = float(re.sub(r'€ Studierende', '', p).replace(',', '.'))
        if "Schüler" in p:
            schueler_price = float(re.sub(r'€ Schüler', '', p).replace(',', '.'))
        if "Mitarbeiter" in p:
            mitarbeiter_price = float(re.sub(r'€ Mitarbeiter', '', p).replace(',', '.'))
        if "Gäste" in p:
            gaeste_price = float(re.sub(r'€ Gäste', '', p).replace(',', '.'))

else:
    student_price = None
    schueler_price = None
    mitarbeiter_price = None
    gaeste_price = None

print("Preise:")
print("Studierende:", student_price)
print("Schüler", schueler_price)
print("Mitarbeiter", mitarbeiter_price)
print("Gäste", gaeste_price)

# Iterate over each tab (day).
for key in dict_of_tabs:

    # Get soup for day.
    day = soup.find('div', {'id': key})

    print("-----------------------------------------------------------------")
    print("On", dict_of_tabs.get(key), "the following meals will be served: ")

    # Find section of soup that gives the Speiseplan.
    speiseplan = day.find_all('div', {'class': 'speiseplanTagKat'})

    # Iterate over each meal option in Speiseplan.
    for i in speiseplan:

        # Extract type/category of meal. E.g. Stammessen, Vegetarisch, etc.
        cat = i.find('div', {'class': 'category'}).get_text()
        cat_clean = re.sub(' +', ' ', re.sub(r'\([^)]*\)', '', cat))
        print("Category:\t", cat_clean)

        # Extract meal name.
        title = i.find('div', {'class': 'title'}).get_text()
        title_clean = re.sub(' +', ' ', re.sub(r'\([^)]*\)', '', title))
        title_exclude_price = re.sub(r'(100g /)* \d,\d\d Euro', '', title_clean)
        alternative_price = re.search(r'(100g /)* \d,\d\d Euro', title_clean)
        title_list = [x.strip() for x in re.split(', | und ', title_exclude_price)]


        if alternative_price is not None:
            alt_price = alternative_price.group(0)
        else:
            alt_price = None

        print("Meal:\t", title_list)



        # Extract meal pricing.
        if i.find('div', {'class': 'preise'}) is not None:
            price = re.sub(' +', ' ', i.find('div', {'class': 'preise'}).get_text()).split(" | ")
            for p in price:
                if "Studierende" in p:
                    student_price = float(re.sub(r'€ Studierende', '', p).replace(',', '.'))
                if "Schüler" in p:
                    schueler_price = float(re.sub(r'€ Schüler', '', p).replace(',', '.'))
                if "Mitarbeiter" in p:
                    mitarbeiter_price = float(re.sub(r'€ Mitarbeiter', '', p).replace(',', '.'))
                if "Gäste" in p:
                    gaeste_price = float(re.sub(r'€ Gäste', '', p).replace(',', '.'))

        else:
            student_price = alt_price
            schueler_price = alt_price
            mitarbeiter_price = alt_price
            gaeste_price = alt_price

        print("Preise:")
        print("Studierende:", student_price)
        print("Schüler", schueler_price)
        print("Mitarbeiter", mitarbeiter_price)
        print("Gäste", gaeste_price)
        print("")

    print(" ")



tuesday = soup.find('div', {'id': 'tab2'})

children = monday.findChildren()
for child in children:
    print("--------------------------")
    if child.find()

tables = soup.find_all('table')
