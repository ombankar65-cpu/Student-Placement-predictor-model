import streamlit as st
import pickle
import numpy as np

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="ML Model Predictor",
    page_icon="🤖",
    layout="centered"
)

# ------------------------------
# Custom CSS for Attractive UI
# ------------------------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }

    .prediction-box {
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #4CAF50;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        background-color: white;
    }

    .title {
        text-align: center;
        color: #4CAF50;
        font-size: 32px;
        font-weight: bold;
    }

    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 45px;
        font-size: 16px;
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------------
# Title
# ------------------------------
st.markdown('<p class="title">Machine Learning Prediction App 🚀</p>', unsafe_allow_html=True)
st.write("Fill the details below to get prediction")

# ------------------------------
# Load Model
# ------------------------------
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# ------------------------------
# Input Section (Edit as per your model)
# ------------------------------
st.markdown('<div class="prediction-box">', unsafe_allow_html=True)

feature1 = st.number_input("Enter Feature 1")
feature2 = st.number_input("Enter Feature 2")
feature3 = st.number_input("Enter Feature 3")

predict_button = st.button("Predict")

st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------
# Prediction
# ------------------------------
if predict_button:
    input_data = np.array([[feature1, feature2, feature3]])
    prediction = model.predict(input_data)

    st.success(f"Prediction Result: {prediction[0]}")
