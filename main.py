import streamlit as st
import plotly.express as px
from back_end import get_weather_data
from pathlib import Path


ASSETS_DIR = Path('./assets')
IMAGES_DIR = ASSETS_DIR / "images"


def get_sample_data(days):
    # Define sample dates and temperatures
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    # Multiply temperatures by the number of days selected
    temperatures = [days * t for t in temperatures]

    # Return dates and adjusted temperatures
    return dates, temperatures


# Display the title
st.title("Weather Forecast for the Next Days")

# Collect user input for location
place_input = st.text_input("Place:", placeholder="Enter a city")

# Collect user input for forecast days using a slider
forecast_days = st.slider("Forecast Days", min_value=1,
                          max_value=5, help="Select the number of forecasted days")

# Allow user to select weather_data type to view ('Temperature' or 'Sky Condition')
weather_option = st.selectbox("Select data to view",
                              options=('Temperature', 'Sky'))

# Check if location is provided (forecast_days and weather_option have default values so always are provided)
if place_input:

    # Get data for the specified number of forecast days
    # dates, temperatures = get_sample_data(forecast_days)
    # dates, temperatures = get_weather_data(place_input, forecast_days, weather_option)
    # Call the function to get weather data for the specified city
    weather_data = get_weather_data(place_input, forecast_days)

    # Check if weather data was successfully retrieved
    if weather_data:

        # Display subheader with location and forecast days
        st.subheader(f"{weather_option} for the next {
            forecast_days} day(s) in {place_input.title()}")

        # Process weather data based on the selected option
        match weather_option:
            # If 'Temperature' option is selected
            case 'Temperature':
                # Extract temperatures and dates from weather data dictionaries
                # Divide temperatures by 10 to make them readable (assuming they are in units of tenths of degrees Celsius)
                temperatures = [a_dict['main']['temp'] / 10
                                for a_dict in weather_data]
                dates = [a_dict['dt_txt'] for a_dict in weather_data]

                # Create a line plot using Plotly Express
                figure = px.line(x=dates, y=temperatures, labels={
                    'x': 'Date', 'y': 'Temperature (C)'})
                # Display the plot using Plotly chart in Streamlit
                st.plotly_chart(figure)

            # If 'Sky' option is selected
            case 'Sky':
                # Extract sky conditions from weather data dictionaries
                sky_conditions = [a_dict['weather'][0]['main']
                                  for a_dict in weather_data]
                # Initialize a list to store paths to sky condition images
                sky_conditions_img_paths = []

                # Iterate over each sky condition in the list
                for condition in sky_conditions:
                    # Construct the path to the corresponding image file based on the condition
                    img_path = IMAGES_DIR / f'{condition.lower()}.png'
                    # Append the path to the list
                    sky_conditions_img_paths.append(str(img_path))

                # Display the images corresponding to the sky conditions
                st.image(sky_conditions_img_paths)

                # # Define the number of columns
                # num_columns = 6

                # # Create columns
                # columns = st.columns(num_columns)

                # # Display images with spacing
                # for i, image_path in enumerate(sky_conditions_img_paths):
                #     with columns[i]:
                #         st.image(image_path)

    else:
        # If data is not available, print an error message indicating that the city was not found
        st.error("Sorry, weather data is currently unavailable. This could be due to the city not being found or a failure to retrieve the data. Please try again later.")
