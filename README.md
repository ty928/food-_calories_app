# food-_calories_app

from nutritionix import Nutritionix
import csv
from dotenv import load_dotenv
import json
import os
import pdb
import requests
import datetime

while True:
    gender = input("Is a male or female: ").lower()
    if gender not in "male" "female":
        print("Check Your Spelling. Expecting 'Male' or 'Female'")
        continue
    else:
        break

while True:
    try:
        weight = int(input("Please input your weight(in pond): "))
    except ValueError:
        print("Sorry, Please Input Number.")
        continue
    if weight < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

while True:
    try:
        height = float(input("Please input your height(in feet): "))
    except ValueError:
        print("Sorry, Please Input Number.")
        continue
    if height < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

while True:
    try:
        age = int(input("Please input your age(eg.25): "))
    except ValueError:
        print("Sorry, Please Input Integer.")
        continue
    if age < 0:
            print("Sorry, your response must not be negative.")
            continue
    else:
        break

print("-------------------------------------------------")
print("Today is ", datetime.datetime.now().strftime("%Y-%B-%d"))
print("The food recommened to you: ")

if gender == "male":
    need_calories = (10 * weight * 0.4536 + 6.25 * height *30.48 - 5 * age + 5) * 1.2
elif gender == "female":
    need_calories = (10 * weight * 0.4536 + 6.25 * height *30.48 - 5 * age - 161) * 1.2


nix = Nutritionix(app_id="8bb7964a", api_key="7df918b6e9c42d80527477223d2fd580")

obj = nix.search().nxql(
    filters={
        "nf_calories": {
            #"lte": 500
            "from":200,
            "to":500
        }
    },
    fields=["item_name", "nf_calories"]
).json()


results = []
for hit in obj['hits']:
    result = {
            "item_name": hit['fields']['item_name'],
            "nf_calories": hit['fields']['nf_calories']
    }
    results.append(result)

#pdb.set_trace()
filter_results = []
total_calories = 0
for result in results:
    total_calories += result["nf_calories"]
    if total_calories <= need_calories:
        filter_results.append(result)
        print("Food Name: " + result['item_name'] + "........" + "Calroies: " + str(result['nf_calories']))

print("-------------------------------------------------")
print("HAVE A NICE DAY. ENJOY YOUR MEAL")


def write_prices_to_file(hits=[], filename="data/food.csv"):
    csv_filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(csv_filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["item_name","calories"])
        writer.writeheader()
        for d in hits:
            row = {
                "item_name": d["item_name"], # change attribute name to match project requirements
                "calories": d["nf_calories"]
            }
            writer.writerow(row)

food_calories = filter_results

write_prices_to_file(hits= food_calories, filename="data/food.csv")



Installation
#pip install nutritionix
 in Command Prompt
Run the application
1.Navigate to the directory in which you saved the file. 
2.To run the program, issue the following command: python nutritions.py
3Note: you must use Python3 to run this program.

