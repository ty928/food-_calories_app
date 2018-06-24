Installation
#pip install nutritionix
Others please reference to pip install -r requirements.txt

Config
You'll need an api key and app id which is tied to a developer account at https://developer.nutritionix.com
You may provide these parameters in your code or with the environment variables NIX_APP_ID & NIX_API_KEY

Usage
Instantiate
First, instantiate the API wrapper object:
from nutritionix import Nutritionix
nix = Nutritionix(app_id="123456789", api_key="XXXYYYZZZ")
Or if you have configured the environment variables, simply:
from nutritionix import Nutritionix
nix = Nutritionix()

Run the application
1.Navigate to the directory in which you saved the file.
2.To run the program, issue the following command: python nutritions.py
3Note: you must use Python3 to run this program.
