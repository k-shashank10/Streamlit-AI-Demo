# app.py
import streamlit as st
import pandas as pd

# Simulated API response
api_response = {
    "train_name": "Rajdhani Express",
    "train_number": "12301",
    "route": [
        {"station": "New Delhi",      "arrival": "Source",      "departure": "07:05"},
        {"station": "Kanpur Central", "arrival": "10:10",       "departure": "10:15"},
        {"station": "Allahabad Jn",   "arrival": "12:00",       "departure": "12:10"},
        {"station": "Patna Jn",       "arrival": "16:30",       "departure": "16:40"},
        {"station": "Howrah Jn",      "arrival": "21:30",       "departure": "Destination"}
    ]
}

# -------------------------------
# Task 1 — Parse the Data
# -------------------------------
# Convert route list into DataFrame
route_data = pd.DataFrame(api_response["route"])
route_data.columns = ["Station", "Arrival", "Departure"]

# -------------------------------
# Task 2 — Build the Streamlit App
# -------------------------------
st.markdown(f"### 🚆 Train: {api_response['train_name']} ({api_response['train_number']})")

# Display full route table
st.dataframe(route_data, use_container_width=True)

# Selectbox for stations
selected_station = st.selectbox("Choose a station:", route_data["Station"].tolist())

# Show arrival and departure for selected station
station_info = route_data[route_data["Station"] == selected_station].iloc[0]
st.text(f"Arrival: {station_info['Arrival']}")
st.text(f"Departure: {station_info['Departure']}")
