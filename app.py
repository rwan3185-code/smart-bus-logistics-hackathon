import streamlit as st
import pandas as pd
import joblib

# إعداد الصفحة
st.set_page_config(
    page_title="Smart Bus Logistics System",
    page_icon="🚌",
    layout="wide"
)

# تحميل المودل
model = joblib.load("bus_model.pkl")

# Sidebar
st.sidebar.title("🚌 Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home", "Prediction", "Analytics"]
)

# =========================
# Home Page
# =========================
if page == "Home":

    st.title("🚌 Smart Bus Logistics System")

    st.markdown("""
    ### AI-powered logistics platform for predicting
    bus delays and breakdown risks.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Active Buses", "120")
    col2.metric("Delay Reports", "35")
    col3.metric("Breakdown Risk", "18%")

    st.image(
        "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957",
        use_container_width=True
    )

# =========================
# Prediction Page
# =========================
elif page == "Prediction":

    st.title("🔍 Bus Breakdown Prediction")

    st.write("Enter Bus Information")

    bus_no = st.number_input("Bus Number", min_value=0)

    route_number = st.number_input("Route Number", min_value=0)

    delay_time = st.number_input(
        "Delay Time (minutes)",
        min_value=0
    )

    # زر التوقع
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

        # ترتيب الأعمدة حسب المودل
        input_data = input_data[model.feature_names_in_]

        prediction = model.predict(input_data)

        # نسبة التأخير المنطقية
        if delay_time < 10:
            delay_percent = 20

        elif delay_time < 30:
            delay_percent = 55

        else:
            delay_percent = 90

        st.warning(
            f"⏰ Expected Delay Probability: {delay_percent:.2f}%"
        )

        # التوقع النهائي
        if prediction[0] == 1:
            st.error("⚠️ Bus Breakdown Expected")

        else:
            st.success("✅ No Breakdown Expected")

# =========================
# Analytics Page
# =========================
elif page == "Analytics":

    st.title("📊 Analytics Dashboard")

    st.subheader("Bus Delay Analysis")

    chart_data = pd.DataFrame({
        'Bus': [1, 2, 3, 4, 5],
        'Delay': [15, 30, 10, 25, 18]
    })

    st.bar_chart(chart_data.set_index('Bus'))

    st.subheader("System Insights")

    col1, col2 = st.columns(2)

    col1.info("🚍 Most delays happen during peak hours.")

    col2.success("✅ Route efficiency improved by 15%.")