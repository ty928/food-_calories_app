import csv
import json
import os
import pdb
import sys

#from app.nu import write_prices_to_file
sys.path.append('./app/')
from nutritions import write_prices_to_file


def test_write_prices_to_file(daily_food):
    # setup:
    write_prices_to_file(hits = daily_food, filename="tests/example_reports/food.csv")
    # test:
    csv_filepath = os.path.join(os.path.dirname(__file__), "example_reports/food.csv")
    rows_written = []
    with open(csv_filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows_written.append(dict(row))
    try:
        assert len(rows_written) == 9
        assert rows_written[0]["item_name"] == "Veal, variety meats and by-products, pancreas, cooked, braised  3 oz"
        assert rows_written[0]["calories"] == "217.6"
        print('No ERROR, and the data is completed!')
        pass
    except Exception as e:
        raise



if __name__ == '__main__':
    daily_food = [

    {"item_name": "Veal, variety meats and by-products, pancreas, cooked, braised  3 oz","calories": "217.6"},

    {"item_name": "Game meat, bison, shoulder clod, separable lean only, trimmed to 0"" fat, raw - 1 lb", "calories": "94.42"},

    {"item_name": "Veal, Australian, shank, hind, bone-in, separable lean and fat - 1 roast with bone", "calories": "475.2"},

    {"item_name": "Bread, french or vienna, toasted (includes sourdough) - 1 slice, large","calories": "280.72"},

    {"item_name": "Cake, chocolate, prepared from recipe without frosting - 1 piece (1/12 of 9"" dia)", "calories": "352.45"},

    {"item_name": "Cake, gingerbread, prepared from recipe - 1 piece (1/9 of 8"" square)", "calories": "263.44"},

    {"item_name": "Cake, pound, commercially prepared, other than all butter, enriched - 1 snack cake (2.5 oz)", "calories": "276.19"},

    {"item_name": "Cheesecake prepared from mix, no-bake type - 1 piece (1/12 of 9"" dia)", "calories": "271.26"},

    {"item_name": "Cookies, brownies, commercially prepared - 1 square, large (2-3/4"" sq x 7/8"")", "calories": "226.8"}
    ]

    test_write_prices_to_file(daily_food)
