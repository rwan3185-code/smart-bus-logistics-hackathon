import streamlit as st
import pandas as pd
import joblib

# تحميل المودل
model = joblib.load("bus_model.pkl")

st.title("🚌 Bus Breakdown Prediction System")

st.write("Enter Bus Information")

# إدخالات المستخدم
bus_no = st.number_input("Bus Number", min_value=0)

route_number = st.number_input("Route Number", min_value=0)

delay_time = st.number_input("Delay Time (minutes)", min_value=0)

# زر التنبؤ
if st.button("Predict"):

    input_data = pd.DataFrame({
        'Bus_No': [bus_no],
        'Route_Number': [route_number],
        'Run_Type': [1],
        'Reason': [1],
        'Boro': [1],
        'Bus_Company_Name': [1],
        'How_Long_Delayed': [delay_time],
        'Number_Of_Students_On_The_Bus': [30]
    })

    input_data = input_data[model.feature_names_in_]

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)

    delay_percent = probability[0][1] * 100

    st.warning(f"⏰ Expected Delay Probability: {delay_percent:.2f}%")

    if prediction[0] == 1:
        st.error("⚠️ Bus Breakdown Expected")

    else:
        st.success("✅ No Breakdown Expected")