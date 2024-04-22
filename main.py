import streamlit as st
import plotly.express as px
from back_end import get_weather_data
from constants import *
from datetime import datetime


def get_sample_data(days):
    # Define sample dates and temperatures
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    # Multiply temperatures by the number of days selected
    temperatures = [days * t for t in temperatures]

    # Return dates and adjusted temperatures
    return dates, temperatures


def combine_conditions_with_dates(sky_conditions, dates):
    """
    Combine sky conditions with their corresponding dates.

    Args:
        sky_conditions (list of str): A list of sky conditions.
        dates (list of str): A list of dates in the format "%Y-%m-%d %H:%M:%S".

    Returns:
        list: A list of dictionaries, each containing 'day' and 'sky' keys. 
              'day' contains formatted dates and 'sky' contains the path to the
              corresponding image file based on the condition.
    """
    # Convert date strings to datetime objects
    date_objects = [datetime.strptime(
        date, "%Y-%m-%d %H:%M:%S") for date in dates]

    # Initialize an empty list to store combined data
    combined = []

    # Iterate over pairs of date objects and sky conditions
    for pair in zip(date_objects, sky_conditions):
        # Format the date as "Mon DD HH:MM"
        formatted_date = pair[0].strftime("%b %d %H:%M")

        # Construct the path to the corresponding image file based on the condition
        condition_img_path = IMAGES_DIR / f'{pair[1].lower()}.png'

        # Create a dictionary representing the combined data
        element = {
            'day': formatted_date,
            'sky': condition_img_path
        }

        # Append the combined data to the list
        combined.append(element)

    return combined


# Display the title
st.title("Weather Forecast for the Next Days")

# Collect user input for location
place_input = st.text_input("Place:", placeholder="Enter a city")

# Collect user input for forecast days using a slider
forecast_days = st.slider("Forecast Days", min_value=1,
                          max_value=5, help="Select the number of forecasted days")

# Allow user to select weather_data type to view ('Temperature' or 'Sky Condition')
weather_option = st.selectbox("Select data to view",
                              options=('Temperature', 'Sky Condition'))

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

            # If 'Sky Condition' option is selected
            case 'Sky Condition':
                # Extract sky conditions and dates from weather data dictionaries
                sky_conditions = [a_dict['weather'][0]['main']
                                  for a_dict in weather_data]
                dates = [a_dict['dt_txt'] for a_dict in weather_data]

                # combine the two data lists `dates` and `sky_conditions`
                dates_with_conditions = combine_conditions_with_dates(
                    sky_conditions, dates)

                # Display images in rows of 8 (each day has 8 intervals) with space between them

                # Loop through the range of indices in increments of 8 (number of intervals per day)
                for i in range(0, len(dates_with_conditions), INTERVALS_PER_DAY):
                    # Slice the list of combined data (dates + conditions) to create a row of up to 8 elements
                    row = dates_with_conditions[i: i+INTERVALS_PER_DAY]

                    # Create columns for the elements in the row (for each element (day+image) a column)
                    columns = st.columns(len(row))

                    # Iterate over the columns and corresponding elements in the row
                    for i, col in enumerate(columns):
                        # Display each element day in its respective column
                        col.write(row[i]['day'])
                        # Display each element image in its respective column, adjusting the width to fit the column
                        # use_column_width=True ensures that the image width is adjusted to fit the width of the column
                        # convert each img path to string using str() to be displayed in st.image()
                        col.image(str(row[i]['sky']), use_column_width=True)

    else:
        # If data is not available, print an error message indicating that the city was not found
        st.error("Sorry, weather data is currently unavailable. This could be due to the city not being found or a failure to retrieve the data. Please try again later.")
