import os
from pathlib import Path
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()


# We can search weather forecast for 5 days with data every 3 hours by city name using this API endpoint.
OPENWEATHERMAP_API_ENDOINT = "https://api.openweathermap.org/data/2.5/forecast"
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

"""
- Study of the data returned from openweathermap API:

    1. Get the total number of intervals/observations (every 3 hours) for 5 days, by default theres 40 intervals

    2. Calculate the number of intervals (observations) per day (dividing by 24 cz 24 hours a day),
       1 interval every 3 hours, so 1 day (24h) / 3h = 8, so there's 8 intervals per day   
       
"""
INTERVALS_PER_DAY = 8


ASSETS_DIR = Path('./assets')
IMAGES_DIR = ASSETS_DIR / "images"
