import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Set page configuration
st.set_page_config(
    page_title="Delivery Time Prediction",
    layout="wide"
)

# Load the model
@st.cache_resource
def load_model():
    return joblib.load("best_gbr_model_v1.pkl")

try:
    model = load_model()
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Define the scaler
scaler = StandardScaler()

# Create header
st.title("Delivery Time Prediction")
st.write("Enter the delivery details below to get a prediction")

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    # Location and Region Information
    st.subheader("Location Details")
    region_id = st.number_input("Region ID", value=0)
    city = st.text_input("City", value="")
    lng = st.number_input("Longitude", value=0.0, format="%.6f")
    lat = st.number_input("Latitude", value=0.0, format="%.6f")
    
    # AOI Information
    st.subheader("Area of Interest")
    aoi_id = st.number_input("AOI ID", value=0)
    aoi_type = st.text_input("AOI Type", value="")
    
    # Time Information
    st.subheader("Time Details")
    hour = st.slider("Hour of Day", 0, 23, 12)
    day_of_week = st.slider("Day of Week (0=Monday)", 0, 6, 0)
    is_weekend = st.checkbox("Is Weekend")

with col2:
    # GPS Information
    st.subheader("GPS Details")
    accept_gps_time = st.number_input("Accept GPS Time", value=0)
    accept_gps_lng = st.number_input("Accept GPS Longitude", value=0.0, format="%.6f")
    accept_gps_lat = st.number_input("Accept GPS Latitude", value=0.0, format="%.6f")
    
    # Delivery Information
    st.subheader("Delivery Details")
    delivery_time = st.number_input("Delivery Time", value=0)
    delivery_gps_time = st.number_input("Delivery GPS Time", value=0)
    delivery_gps_lng = st.number_input("Delivery GPS Longitude", value=0.0, format="%.6f")
    delivery_gps_lat = st.number_input("Delivery GPS Latitude", value=0.0, format="%.6f")
    
    # Distance
    st.subheader("Distance")
    distance_km = st.number_input("Distance (km)", value=0.0, min_value=0.0, format="%.2f")

# Create predict button
if st.button("Predict Delivery Time"):
    # Create input data dictionary
    input_data = {
        'region_id': region_id,
        'city': city,
        'lng': lng,
        'lat': lat,
        'aoi_id': aoi_id,
        'aoi_type': aoi_type,
        'accept_gps_time': accept_gps_time,
        'accept_gps_lng': accept_gps_lng,
        'accept_gps_lat': accept_gps_lat,
        'delivery_time': delivery_time,
        'delivery_gps_time': delivery_gps_time,
        'delivery_gps_lng': delivery_gps_lng,
        'delivery_gps_lat': delivery_gps_lat,
        'distance_km': distance_km,
        'hour': hour,
        'day_of_week': day_of_week,
        'is_weekend': 1 if is_weekend else 0
    }
    
    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])
    
    try:
        # Make prediction
        prediction = model.predict(input_df)
        
        # Display results
        st.success("Prediction completed!")
        st.subheader("Results")
        st.write(f"Predicted Delivery Time: {prediction[0]:.2f}")
        
        # Display input features
        with st.expander("Show input features"):
            st.json(input_data)
            
    except Exception as e:
        st.error(f"Error making prediction: {e}")

# Add information about the features
with st.expander("Feature Information"):
    st.markdown("""
    ### Feature Descriptions:
    - **Region ID**: Unique identifier for the delivery region
    - **City**: Name of the city
    - **Longitude/Latitude**: Geographic coordinates
    - **AOI ID**: Area of Interest identifier
    - **AOI Type**: Type of Area of Interest
    - **GPS Details**: GPS coordinates and timestamps for acceptance and delivery
    - **Distance**: Distance in kilometers
    - **Time Details**: Hour of day, day of week, and weekend status
    """) 