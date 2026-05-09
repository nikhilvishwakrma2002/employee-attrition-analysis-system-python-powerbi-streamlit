import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time


# ========================================
# PAGE CONFIG
# ========================================

st.set_page_config(
    page_title="EAAS",
    page_icon="📊",
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
# LOADING SCREEN
# ========================================

with st.spinner("Loading EAAS Analytics..."):
    time.sleep(1)


# ========================================
# LOTTIE FUNCTION
# ========================================

def load_lottie(url):

    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.json()


# ========================================
# LOTTIE ANIMATION
# ========================================

lottie_dashboard = load_lottie(
    "https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json"
)


# ========================================
# SIDEBAR
# ========================================

st.sidebar.title("📊 EAAS")

st.sidebar.markdown(
    "AI-Powered Employee Attrition Analytics"
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
Built using:

- Python
- Machine Learning
- Power BI
- Streamlit
"""
)


# ========================================
# HERO SECTION
# ========================================

st.markdown(
"""
# 📊 EAAS

### Employee Attrition Analysis System

#### AI-Powered HR Analytics Platform
"""
)

# ========================================
# LOTTIE CONTAINER
# ========================================

st.markdown(
"""
<div class="lottie-container">
""",
unsafe_allow_html=True
)

st_lottie(
    lottie_dashboard,
    height=300,
    key="dashboard_animation"
)

st.markdown(
"""
</div>
""",
unsafe_allow_html=True
)


# ========================================
# PLATFORM OVERVIEW
# ========================================

st.markdown(
"""
### 🚀 Platform Overview

EAAS helps organizations:

- Analyze employee attrition trends
- Predict employee turnover risks
- Generate HR insights
- Improve workforce decision-making
- Identify high-risk employees
"""
)


# ========================================
# KPI SECTION
# ========================================

st.markdown("## 📈 Key Metrics")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.metric(
        label="Total Employees",
        value="1470"
    )

with col2:
    st.metric(
        label="Attrition Rate",
        value="16.12%"
    )

with col3:
    st.metric(
        label="Average Salary",
        value="$6.5K"
    )


# ========================================
# TABS
# ========================================

tab1, tab2, tab3 = st.tabs([
    "📊 Dashboard",
    "🔮 Prediction",
    "📈 Insights"
])


# ========================================
# DASHBOARD TAB
# ========================================

with tab1:

    st.subheader("Executive HR Dashboard")

    st.write(
        """
        - Employee turnover
        - Department attrition
        - Salary insights
        - Workforce trends
        """
    )


# ========================================
# PREDICTION TAB
# ========================================

with tab2:

    st.subheader("Attrition Prediction System")

    st.write(
        """
        Predict whether an employee
        is likely to leave the company.
        """
    )


# ========================================
# INSIGHTS TAB
# ========================================

with tab3:

    st.subheader("Business Insights")

    st.write(
        """
        - Overtime employees show higher attrition
        - Lower salary bands have higher turnover
        - Job satisfaction impacts retention strongly
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