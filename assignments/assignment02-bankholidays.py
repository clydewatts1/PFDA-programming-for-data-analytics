#---------------------------------------------------------------------------
# File: assignment02-bankholidays.py
# Author: Clyde Watts
# Date: 2025-10-02
# Description: THis assinment will read in and print out UK bank holidays
#              It will also print out the unique bank holidays for Northern Ireland
#---------------------------------------------------------------------------
# Requirements:
# Northern bank holidays
#Write a program called assignment02-bankholidays.py
#The program should print out the dates of the bank holidays that happen in northern Ireland.
#Last few marks (ie this is more tricky)

import json
import os
import requests

# This the website address for irish bank holidays in json format
url_bank_holidays = "https://xwww.gov.uk/bank-holidays.json"

print("Assignment 02 - Bank Holidays")
print("------------------------------------")
print("\n")

print("Fetching data from:", url_bank_holidays)
# Try and get data from website 
try:
    save_file_name = "data/bankholidays.json"
    print("Fetching bank holidays data...")
    print(f"  From {url_bank_holidays}")
    response = requests.get(url_bank_holidays)
    data = response.json()
    print("  Loaded bank holidays data successfully")
    # write data to file
    print(f"  Writing bank holidays data to file {save_file_name}")
    os.makedirs("data", exist_ok=True)
    with open(save_file_name, "w") as f:
        json.dump(data, f, indent=4)
    print("  Wrote bank holidays data successfully")
# Check if there are errors
except requests.RequestException as e:
    print(f"Error fetching bank holidays: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except FileNotFoundError as e:
     print(f"FileNotFoundError {e}")

# Possible data paths
data_paths = ['data','../data','../../data']
data_path = ''
file_name = 'bankholidays.json'


print("All Bank Holidays")
print("------------------------------------")
# find the path to the data file by looping through possible paths
file_name_and_path = None
for path in data_paths:
    file_name_and_path = f"{path}/{file_name}"
    if os.path.isfile(file_name_and_path):
        data_path = path
        break

if  file_name_and_path is None:
    print("Data file not found")
    exit(1)

print(f"Using data file: {file_name_and_path}")


holidays = {}
try: 
    file_name_and_path = f"{data_path}/{file_name}"
    with open(file_name_and_path,"r") as f:
        holidays = json.load(f)
except json.JSONDecodeError as e:
    print(f"Json Error {e}")
    exit(1)
except UnicodeDecodeError as e:
    print(f"UnicodeDecodeError {e}")
    exit(1)
except FileNotFoundError as e:
    print(f"FileNotFoundError {e}")
    exit(1)


# if holidays is empty, we did not find the file
holidays_by_date = {}
# print header
print(f"{'Country':<30} : {'Date':<10} :  {'Holiday':<40} : {'Bunting     '}: Note")
print("-----------------------------  : ---------- :  ---------------------------------------- : ------------: ----")
# loop through countries and holidays
for country in holidays:
    for holiday in holidays[country]['events']:
        print(f"{country:<30} : {holiday['date']} : {holiday['title']:<40} : {'Bunting   ' if holiday['bunting'] else 'No Bunting'} : {holiday['notes']}")
        # add date to dictionary if missing
        if holiday['date'] not in holidays_by_date:
            holidays_by_date[holiday['date']] = {}
        # add country to date and add dictionary
        # use this later to check for unique northern ireland holidays
        # this acts like a indexed list
        holidays_by_date[holiday['date']][country] = holiday


print("")
print("Northern Ireland Only Bank Holidays")
print("------------------------------------")
# print header
print(f"{'Country':<30} : {'Date':<10} :  {'Holiday':<40} : {'Bunting    '}: Note")
print("-----------------------------  : ---------- :  -----------------------------------------: ---------- : ------------------")
# loop through dates and countries
for the_date,holidays_country in holidays_by_date.items():
    # if the country is northern ireland and the count is 1  (ie unique)
    if 'northern-ireland' in holidays_country and len(holidays_country) == 1:
        print(f"{'northern-ireland':<30} : {holidays_country['northern-ireland']['date']} : {holidays_country['northern-ireland']['title']:<40} {' : Bunting   ' if holidays_country['northern-ireland']['bunting'] else ' : No Bunting'} : {holidays_country['northern-ireland']['notes']}")

# End of program