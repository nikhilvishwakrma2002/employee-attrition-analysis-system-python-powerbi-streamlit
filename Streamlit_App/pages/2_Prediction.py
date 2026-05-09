import streamlit as st
import pandas as pd
import time
from utils.prediction import predict_attrition


# ========================================
# PAGE CONFIG
# ========================================

st.set_page_config(
    page_title="Prediction",
    page_icon="🔮",
    layout="wide"
)


# ========================================
# LOAD CSS
# ========================================

def load_css():

    with open(
        r"X:\CODES\PROJECTS\NXDAXEAAS01_Employee_Attrition_Analytics_System_050726\Streamlit_App\assets\styles\style.css"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


# ========================================
# PAGE ANIMATION
# ========================================

st.markdown(
"""
<div class="page-enter-animation">
""",
unsafe_allow_html=True
)


# ========================================
# HERO SECTION
# ========================================

st.markdown(
"""
# 🔮 Attrition Prediction Engine

### AI-Powered Employee Risk Detection System

Predict whether an employee is likely to leave
the organization using machine learning insights.
"""
)


# ========================================
# INPUT SECTION
# ========================================

st.markdown("## 🧾 Employee Information")

col1, col2 = st.columns(2)

with col1:

    age = st.slider(
        "Age",
        18,
        60,
        30
    )

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=50000,
        value=5000
    )

    distance = st.slider(
        "Distance From Home",
        1,
        30,
        5
    )

with col2:

    years = st.slider(
        "Years At Company",
        0,
        40,
        5
    )

    job_satisfaction = st.slider(
        "Job Satisfaction",
        1,
        4,
        2
    )

    overtime = st.selectbox(
        "OverTime",
        ["Yes", "No"]
    )


# ========================================
# PREDICT BUTTON
# ========================================

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 Predict Attrition Risk"):

    with st.spinner("Analyzing Employee Data..."):

        time.sleep(2)

        overtime_value = 1 if overtime == "Yes" else 0

        input_data = {
            "Age": age,
            "MonthlyIncome": monthly_income,
            "DistanceFromHome": distance,
            "YearsAtCompany": years,
            "JobSatisfaction": job_satisfaction,
            "OverTime": overtime_value
        }

        prediction, probability = predict_attrition(
            input_data
        )


    st.markdown("---")


    # ========================================
    # RESULT
    # ========================================

    if prediction == 1:

        st.error(
            "⚠️ High Attrition Risk Detected"
        )

        st.markdown(
            """
            ### Risk Factors

            - Employee may leave the organization
            - Retention strategy recommended
            - HR intervention advised
            """
        )

    else:

        st.success(
            "✅ Low Attrition Risk"
        )

        st.markdown(
            """
            ### Positive Indicators

            - Employee likely to stay
            - Stable engagement level
            - Healthy retention probability
            """
        )


    # ========================================
    # PROBABILITY
    # ========================================

    st.markdown("## 📈 Prediction Probability")

    st.progress(float(probability))

    st.metric(
        "Prediction Confidence",
        f"{round(probability * 100, 2)}%"
    )


# ========================================
# SIDEBAR
# ========================================

st.sidebar.title("🔮 EAAS")

st.sidebar.info(
"""
Employee Attrition Analysis System

AI-Based HR Analytics Platform
"""
)

st.sidebar.markdown("---")

st.sidebar.success(
"""
Prediction Module Active
"""
)


# ========================================
# FOOTER
# ========================================

st.markdown("---")

st.caption(
"""
Developed by Nikhil Kumar Vishwakrma
"""
)

st.markdown(
"""
</div>
""",
unsafe_allow_html=True
)