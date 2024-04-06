import streamlit as st


# st.set_page_config(layout="wide")

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
    if location_input.strip().isalpha() and location_input.strip() != "":
        # Display subheader with location and forecast days
        st.subheader(f"{view_option} for the next {
                     days_input} day(s) in {location_input.title()}")
        # Placeholder for displaying the plot
        st.pyplot()
    else:
        # Invalid location
        st.error("Invalid location. Please enter a valid city name.")
