import requests
from constants import *


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

        # Calculate the number of intervals (observations) based on the number of forecast days
        num_intervals = forecast_days * INTERVALS_PER_DAY

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
