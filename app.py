import streamlit as st
from rainfall_data import get_rainfall
from rainwater_calc import calculate_rainwater
from weather_api import get_current_rainfall
import matplotlib.pyplot as plt
import numpy as np

# App title
st.title("💧 Rainwater Harvesting Estimator (Bangladesh)")

# Sidebar for user input
st.sidebar.header("🌧️ User Input Parameters")

city = st.sidebar.selectbox(
    "Select your city",
    ("Dhaka", "Chittagong", "Khulna", "Sylhet", "Rajshahi")
)

area = st.sidebar.number_input("Rooftop area (m²)", min_value=10.0, max_value=1000.0, value=100.0)
efficiency = st.sidebar.slider("Collection efficiency (%)", 50, 100, 85) / 100  # e.g., 85% → 0.85

use_live = st.sidebar.checkbox("Use live rainfall data (requires internet)", value=False)

# Get rainfall
if use_live:
    rainfall = get_current_rainfall(city)
    if rainfall is None:
        st.warning("⚠️ Couldn't fetch live data. Using static average instead.")
        rainfall = get_rainfall(city) / 365  # Convert to daily mm
        source = "Static (daily avg)"
    else:
        source = "Live (last 1 hour)"
else:
    rainfall = get_rainfall(city) / 365  # Convert to daily mm
    source = "Static (daily avg)"

# Calculate collected water
collected = calculate_rainwater(area, rainfall, efficiency)

# Show results
st.markdown(f"### 📍 City: **{city}**")
st.markdown(f"☔ Rainfall source: **{source}**")
st.markdown(f"🏠 Rooftop area: **{area} m²**")
st.markdown(f"💧 Rainfall: **{rainfall:.2f} mm**")
st.markdown(f"⚙️ Efficiency: **{efficiency*100:.0f}%**")
st.success(f"Estimated Rainwater Collected: **{collected:.2f} Liters**")

# Optional pie chart
labels = ['Captured Water', 'Lost Water']
lost = area * rainfall * (1 - efficiency)
sizes = [collected, lost]
sizes = np.nan_to_num(sizes, nan=0)  # Handle potential NaNs

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#3498db', '#e74c3c'])
ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
st.pyplot(fig)
