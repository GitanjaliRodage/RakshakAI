import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="RakshakAI Crime Map")

st.title("🗺️ Geospatial Crime Intelligence")

data = pd.DataFrame({
    "City": ["Pune", "Mumbai", "Delhi", "Bangalore"],
    "Latitude": [18.5204, 19.0760, 28.6139, 12.9716],
    "Longitude": [73.8567, 72.8777, 77.2090, 77.5946],
    "Cases": [120, 300, 250, 180]
})

m = folium.Map(
    location=[22.5, 78.9],
    zoom_start=5
)

for _, row in data.iterrows():
    folium.Marker(
        [row["Latitude"], row["Longitude"]],
        popup=f"{row['City']} - Cases: {row['Cases']}",
        tooltip=row["City"]
    ).add_to(m)

st_folium(m, width=900, height=500)