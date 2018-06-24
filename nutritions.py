from nutritionix import Nutritionix
import csv
from dotenv import load_dotenv
import json
import os
import pdb
import requests
import datetime



print("-------------------------------------------------")
print("Today is ", datetime.datetime.now().strftime("%Y-%B-%d"))
print("The food recommened to you: ")



nix = Nutritionix(app_id="", api_key="")

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
    if total_calories <= 2000:
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

