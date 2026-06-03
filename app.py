import streamlit as st
import pandas as pd
import joblib

# ================================
# Load Model and Scaler
# ================================

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# ================================
# App Title
# ================================

st.title("Heart Attack Risk Prediction App")

st.write("Enter patient information to predict heart attack risk.")

# ================================
# User Inputs
# ================================

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=30
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=100,
    max_value=500,
    value=200
)

heart_rate = st.number_input(
    "Heart Rate",
    min_value=40,
    max_value=200,
    value=80
)

blood_pressure = st.number_input(
    "Blood Pressure",
    min_value=50,
    max_value=250,
    value=120
)

diabetes = st.selectbox(
    "Diabetes",
    [0, 1]
)

smoking = st.selectbox(
    "Smoking",
    [0, 1]
)

obesity = st.selectbox(
    "Obesity",
    [0, 1]
)

# ================================
# Feature Engineering
# ================================

# Age Group
if age <= 30:
    age_young = 1
    age_senior = 0
    age_elder = 0

elif age <= 50:
    age_young = 0
    age_senior = 0
    age_elder = 0

elif age <= 70:
    age_young = 0
    age_senior = 1
    age_elder = 0

else:
    age_young = 0
    age_senior = 0
    age_elder = 1

# Cholesterol Level
if cholesterol < 200:
    chol_borderline = 0
    chol_high = 0

elif cholesterol <= 240:
    chol_borderline = 1
    chol_high = 0

else:
    chol_borderline = 0
    chol_high = 1

# ================================
# Create Input DataFrame
# ================================

input_data = pd.DataFrame({
    'Age': [age],
    'Cholesterol': [cholesterol],
    'Heart Rate': [heart_rate],
    'Blood Pressure': [blood_pressure],
    'Diabetes': [diabetes],
    'Smoking': [smoking],
    'Obesity': [obesity],

    'Age_Group_Senior': [age_senior],
    'Age_Group_Elder': [age_elder],

    'Cholesterol_Level_Borderline': [chol_borderline],
    'Cholesterol_Level_High': [chol_high]
})

# ================================
# Scale Data
# ================================

input_scaled = scaler.transform(input_data)

# ================================
# Prediction
# ================================

if st.button("Predict"):

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("The patient has a HIGH risk of heart attack.")

    else:
        st.success("The patient has a LOW risk of heart attack.")