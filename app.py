import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Campus Placement Predictor",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for borders and styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .prediction-card {
        padding: 20px;
        border: 2px solid #007bff;
        border-radius: 10px;
        background-color: white;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the model
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as file:
        return pickle.load(file)

model = load_model()

# Header Section
st.title("🎓 Student Placement Predictor")
st.markdown("Enter student academic details below to predict placement probability.")
st.divider()

# Input Layout using Columns and Borders
with st.container():
    st.subheader("📊 Academic Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
        ssc_p = st.number_input("10th Percentage (ssc_p)", min_value=0.0, max_value=100.0, value=65.0)
        hsc_p = st.number_input("12th Percentage (hsc_p)", min_value=0.0, max_value=100.0, value=65.0)
        
    with col2:
        hsc_s = st.selectbox("12th Stream (hsc_s)", options=[0, 1, 2], format_func=lambda x: ["Commerce", "Science", "Arts"][x])
        degree_p = st.number_input("Degree Percentage", min_value=0.0, max_value=100.0, value=65.0)
        mba_p = st.number_input("MBA Percentage", min_value=0.0, max_value=100.0, value=65.0)

st.divider()

# Prediction Logic
if st.button("Predict Placement Status"):
    # Prepare input array based on model feature names 
    # ['gender', 'ssc_p', 'hsc_p', 'hsc_s', 'degree_p', 'mba_p']
    features = np.array([[gender, ssc_p, hsc_p, hsc_s, degree_p, mba_p]])
    
    prediction = model.predict(features)
    probability = model.predict_proba(features)

    # Output Section
    st.subheader("Results")
    
    if prediction[0] == "Placed":
        st.balloons()
        st.success(f"### Result: {prediction[0]}")
        st.markdown(f"**Confidence Score:** {max(probability[0])*100:.2f}%")
    else:
        st.error(f"### Result: {prediction[0]}")
        st.markdown(f"**Improvement suggested.** Confidence Score: {max(probability[0])*100:.2f}%")
