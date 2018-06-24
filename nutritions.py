from nutritionix import Nutritionix
import csv
from dotenv import load_dotenv
import json
import os
import pdb
import requests
import datetime



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
