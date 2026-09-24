import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/delivery_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Food Delivery Time Prediction",
    page_icon="🍔",
    layout="centered"
)

st.title("🍔 Food Delivery Time Prediction")
st.write("Enter the delivery details below to estimate the delivery time.")

# User inputs

age = st.number_input(
    "Delivery Person Age",
    min_value=15,
    max_value=50,
    value=30
)

rating = st.number_input(
    "Delivery Person Rating",
    min_value=1.0,
    max_value=6.0,
    value=4.5,
    step=0.1
)

temperature = st.number_input(
    "Temperature",
    min_value=0.0,
    max_value=50.0,
    value=23.0
)

humidity = st.number_input(
    "Humidity",
    min_value=0.0,
    max_value=100.0,
    value=66.0
)

precipitation = st.number_input(
    "Precipitation",
    min_value=0.0,
    value=0.0
)

distance = st.number_input(
    "Distance (km)",
    min_value=0.0,
    value=10.0
)

traffic = st.selectbox(
    "Traffic Level",
    ["Low", "Moderate", "High", "Very High", "Very Low"]
)

weather = st.selectbox(
    "Weather",
    [
        "clear sky",
        "haze",
        "mist",
        "broken clouds",
        "light rain",
        "smoke",
        "scattered clouds",
        "overcast clouds",
        "fog",
        "few clouds",
        "moderate rain"
    ]
)

order_type = st.selectbox(
    "Type of Order",
    ["Snack", "Meal", "Drinks", "Buffet"]
)

vehicle = st.selectbox(
    "Type of Vehicle",
    ["motorcycle", "scooter", "electric_scooter", "bicycle"]
)

# Prediction button

if st.button("Predict Delivery Time"):

    input_data = pd.DataFrame({
        "Delivery_person_Age": [age],
        "Delivery_person_Ratings": [rating],
        "temperature": [temperature],
        "humidity": [humidity],
        "precipitation": [precipitation],
        "Distance (km)": [distance],
        "Traffic_Level": [traffic],
        "weather_description": [weather],
        "Type_of_order": [order_type],
        "Type_of_vehicle": [vehicle]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Delivery Time: {prediction:.1f} minutes"
    )