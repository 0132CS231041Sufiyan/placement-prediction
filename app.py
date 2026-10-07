
import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("🎓 Placement Prediction")
st.write("Enter your CGPA and IQ to predict placement.")

cgpa = st.number_input("Enter CGPA", min_value=0.0, max_value=10.0, value=7.0)
iq = st.number_input("Enter IQ", min_value=50, max_value=200, value=100)

if st.button("Predict"):
    input_data = np.array([[cgpa, iq]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("🎉 Student is likely to be Placed!")
    else:
        st.error("❌ Student is likely to be Not Placed.")
