import streamlit as st
import plotly.express as px


def get_data(days):
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
location_input = st.text_input("Place:", placeholder="Enter a city")

# Collect user input for forecast days using a slider
days_input = st.slider("Forecast Days", min_value=1,
                       max_value=5, help="Select the number of forecasted days")

# Allow user to select data to view
view_option = st.selectbox("Select data to view",
                           options=('Temperature', 'Sky'))

# Check if both location and forecast days are provided
if location_input and days_input and view_option:
    # Check if location_input is a valid name
    if location_input.strip().isalpha():
        # Display subheader with location and forecast days
        st.subheader(f"{view_option} for the next {
                     days_input} day(s) in {location_input.title()}")

        # Get data for the specified number of forecast days
        dates, temperatures = get_data(days_input)

        # Create a line plot using Plotly Express
        figure = px.line(x=dates, y=temperatures, labels={
                         'x': 'Date', 'y': 'Temperature (C)'})
        # Display the plot using Plotly chart in Streamlit
        st.plotly_chart(figure)
    else:
        # Invalid location
        st.error("Invalid location. Please enter a valid city name.")
