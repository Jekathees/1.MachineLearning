# Multiple Disease Prediction System using Streamlit

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np


# Page Configuration

st.set_page_config(
    page_title="Health Assistant",
    layout="wide",
    page_icon="🧑‍⚕️"
)


# Working Directory

working_dir = os.path.dirname(os.path.abspath(__file__))


# Load Saved Models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))


# Sidebar Navigation

with st.sidebar:
    selected_page = option_menu(
        "Multiple Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"],
        menu_icon="hospital-fill",
        icons=["activity", "heart", "person"],
        default_index=0
    )


# Diabetes Prediction Page

if selected_page == "Diabetes Prediction":
    st.title("Diabetes Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input("Number of Pregnancies")
        skin_thickness = st.text_input("Skin Thickness value")
        diabetes_pedigree = st.text_input("Diabetes Pedigree Function value")

    with col2:
        glucose = st.text_input("Glucose Level")
        insulin = st.text_input("Insulin Level")
        age = st.text_input("Age of the Person")

    with col3:
        blood_pressure = st.text_input("Blood Pressure value")
        bmi = st.text_input("BMI value")

    diabetes_result = ""
    if st.button("Diabetes Test Result"):
        try:
            input_features = [float(x) for x in [
                pregnancies, glucose, blood_pressure, skin_thickness,
                insulin, bmi, diabetes_pedigree, age
            ]]
            prediction = diabetes_model.predict([input_features])
            diabetes_result = "The person is diabetic" if prediction[0] == 1 else "The person is not diabetic"
        except:
            diabetes_result = "Please enter valid numeric values"

    st.success(diabetes_result)


# Heart Disease Prediction Page

if selected_page == "Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
        trestbps = st.text_input("Resting Blood Pressure")
        restecg = st.text_input("Resting Electrocardiographic results")
        oldpeak = st.text_input("ST depression induced by exercise")
        ca = st.text_input("Major vessels colored by fluoroscopy")

    with col2:
        sex = st.text_input("Sex (0 = female, 1 = male)")
        chol = st.text_input("Serum Cholesterol in mg/dl")
        thalach = st.text_input("Maximum Heart Rate achieved")
        slope = st.text_input("Slope of the peak exercise ST segment")
        thal = st.text_input("Thal: 0=normal,1=fixed,2=reversable")

    with col3:
        cp = st.text_input("Chest Pain type")
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl")
        exang = st.text_input("Exercise Induced Angina")

    heart_result = ""
    if st.button("Heart Disease Test Result"):
        try:
            input_features = [float(x) for x in [
                age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                exang, oldpeak, slope, ca, thal
            ]]
            prediction = heart_model.predict([input_features])
            heart_result = "The person has heart disease" if prediction[0] == 1 else "The person does not have any heart disease"
        except:
            heart_result = "Please enter valid numeric values"

    st.success(heart_result)


# Parkinson's Prediction Page

if selected_page == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
        RAP = st.text_input("MDVP:RAP")
        shimmer_apq3 = st.text_input("Shimmer:APQ3")
        HNR = st.text_input("HNR")
        D2 = st.text_input("D2")

    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
        PPQ = st.text_input("MDVP:PPQ")
        shimmer_apq5 = st.text_input("Shimmer:APQ5")
        RPDE = st.text_input("RPDE")
        PPE = st.text_input("PPE")

    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
        DDP = st.text_input("Jitter:DDP")
        APQ = st.text_input("MDVP:APQ")
        spread1 = st.text_input("spread1")

    with col4:
        jitter_percent = st.text_input("MDVP:Jitter(%)")
        shimmer = st.text_input("MDVP:Shimmer")
        DDA = st.text_input("Shimmer:DDA")
        spread2 = st.text_input("spread2")

    with col5:
        jitter_abs = st.text_input("MDVP:Jitter(Abs)")
        shimmer_db = st.text_input("MDVP:Shimmer(dB)")

    parkinsons_result = ""
    if st.button("Parkinson's Test Result"):
        try:
            input_features = [
                fo, fhi, flo, jitter_percent, jitter_abs,
                RAP, PPQ, DDP, shimmer, shimmer_db, shimmer_apq3,
                shimmer_apq5, APQ, DDA, HNR, RPDE, spread1,
                spread2, D2, PPE
            ]
            input_features = [float(x) for x in input_features]
            prediction = parkinsons_model.predict([input_features])
            parkinsons_result = "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
        except:
            parkinsons_result = "Please enter valid numeric values"

    st.success(parkinsons_result)
