# Forecast Finder

## Overview
Forecast Finder is an intuitive application built with `Streamlit` and `Plotly`, designed to provide accurate weather forecast data for the upcoming days. Users can easily input a city name and select the desired number of forecast days to receive detailed information on temperature trends and sky conditions, making it a convenient tool for planning ahead.

## Features
- **Interactive Interface**: Users can input a city name and select the number of forecast days using sliders and dropdown menus.
- **Temperature Visualization**: The app displays a line plot showing the temperature forecast for the selected city and days.
- **Sky Condition Visualization**: Users can view images representing the sky condition forecast for each interval of the selected days.

## Technologies Used
- **plotly**: A graphing library for interactive plots.
- **python-dotenv**: A library for managing environment variables in `.env` files.
- **requests**: A library for making HTTP requests.
- **streamlit**: An app framework for creating and sharing data apps.
- **datetime**: A module for manipulating dates and times.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Obtain an API key from [OpenWeatherMap API](https://openweathermap.org/api) by signing up for an account and subscribing to their API services.
5. Configure the necessary parameters such as the obtained API key in `constants.py`.
   - Set the API key as the value of `OPENWEATHERMAP_API_KEY`.
6. Run the script using `streamlit run main.py`.

## Usage
1. Run the script using `streamlit run main.py`.
2. Enter the name of the city for which you want to view the weather forecast.
3. Use the slider to select the number of days for the forecast.
4. Choose whether to view temperature or sky condition data.
5. The app will display the weather forecast accordingly.

## OpenWeatherMap API
- Weather Forecast App utilizes the OpenWeatherMap API to retrieve weather data. This API provides current weather data, forecasts, and historical weather data for any location. By signing up for an account and subscribing to their API services, users can obtain an API key required for accessing the data.
- The data returned from the OpenWeatherMap API is structured in intervals of every 3 hours for up to 5 days. By default, there are 40 intervals, representing 5 days of forecast data.
    1. To process the data, the total number of intervals/observations for 5 days is obtained, which is 40 by default.
    2. The number of intervals (observations) per day is calculated by dividing the total number of intervals by the number of hours in a day (24). Since there is an interval every 3 hours, there are 8 intervals per day.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.