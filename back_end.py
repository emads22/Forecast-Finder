import requests
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()


# We can search weather forecast for 5 days with data every 3 hours by city name using this API endpoint.
OPENWEATHERMAP_API_ENDOINT = "https://api.openweathermap.org/data/2.5/forecast"
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")


def get_weather_data(city, forecast_days):
    """
    Fetches weather forecast data from the OpenWeatherMap API for a specific city.

    Parameters:
        city (str): The name of the city for which weather data is requested.
        forecast_days (int): Number of forecast days to retrieve.

    Returns:
        dict or None: Weather forecast data in JSON format if successful, otherwise None.
    """
    # Make a GET request to the OpenWeatherMap API to fetch weather data
    response = requests.get(
        f"{OPENWEATHERMAP_API_ENDOINT}?q={city}&appid={OPENWEATHERMAP_API_KEY}")

    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        # Convert response data to JSON format
        data = response.json()

        # Extract weather data for the specified number of days
        # Calculate the number of intervals (observations) based on the number of days
        # By default theres 40 intervals cz 5 days, and 5 * 8 = 40
        # 8 intervals per day (every 3 hours, so 1 day: 24h / 3h = 8)
        intervals_per_day = 8
        num_intervals = forecast_days * intervals_per_day

        # Filter the data to include only the required number of intervals
        filtered_data = data["list"][:num_intervals]

        return filtered_data

    # If response status code is not 200, return None
    return None


def main():
    city = 'Tokyo'
    this_weather_data = get_weather_data(city, 2)

    if this_weather_data:
        print(this_weather_data)
    else:
        print("\nCity Not Found\n")


if __name__ == '__main__':
    main()
