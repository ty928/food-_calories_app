# Food Calories Recommendation APP
Take a user input information of age, gender, weight and height and output food recommendation daily to help user have healthy and various food.
## Installation
 #pip install nutritionix
 
 #Pipenv on Mac or Windows:
pipenv install -r requirements.txt

#Homebrew-installed Python 3.x on Mac OS:
pip3 install -r requirements.txt

#All others:
pip install -r requirements.txt

Others please reference to pip install -r requirements.txt

## Setup
### Environment Variables
 You'll need an api key and app id which is tied to a developer account at https://developer.nutritionix.com
 
 You may provide these parameters in your code or with the environment variables NIX_APP_ID & NIX_API_KEY


#### First, instantiate the API wrapper object:
from nutritionix import Nutritionix

nix = Nutritionix(app_id="123456789", api_key="XXXYYYZZZ")
#### Or if you have configured the environment variables, simply:
from nutritionix import Nutritionix

nix = Nutritionix()

## Usage
 1.Navigate to the directory in which you saved the file.
 
 2.To run the program, issue the following command: python nutritions.py
 
 3.Note: you must use Python3 to run this program.
 Testing

## Testing
Run tests:

pytest
