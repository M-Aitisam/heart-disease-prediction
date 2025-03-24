import streamlit as st
import numpy as np
import joblib

# -------------------------
# Load the trained model
# -------------------------
try:
    model = joblib.load("heart_disease_model.pkl")
    if not hasattr(model, "predict"):
        st.error("❌ Loaded file is not a valid model. Please check 'heart_disease_model.pkl'.")
        model = None
except Exception as e:
    st.error(f"Error loading model: {e}")
    model = None

# -------------------------
# Streamlit App UI
# -------------------------
st.title("❤️ Heart Disease Prediction App")

st.write("Enter patient details below:")

# -------------------------
# User Input Form
# -------------------------
features = []

feature_labels = [
    "Age", "Sex (1=Male, 0=Female)", "Chest Pain Type", "Resting Blood Pressure",
    "Cholesterol", "Fasting Blood Sugar (1=True, 0=False)", "Resting ECG",
    "Max Heart Rate", "Exercise-Induced Angina (1=True, 0=False)", "ST Depression",
    "Slope of ST Segment", "Number of Major Vessels", "Thalassemia", "Extra Feature 1", "Extra Feature 2"
]

for label in feature_labels:
    value = st.number_input(label, min_value=0.0, format="%.2f")
    features.append(value)

# -------------------------
# Prediction
# -------------------------
if st.button("Predict"):
    if model:
        input_features = np.array(features).reshape(1, -1)

        try:
            prediction = model.predict(input_features)[0]
            result = "⚠️ High Risk of Heart Disease" if prediction == 1 else "✅ Low Risk of Heart Disease"
            st.subheader(f"Prediction: {result}")
        except Exception as e:
            st.error(f"Error making prediction: {e}")
    else:
        st.error("❌ Model is not loaded. Please check 'heart_disease_model.pkl'.")
