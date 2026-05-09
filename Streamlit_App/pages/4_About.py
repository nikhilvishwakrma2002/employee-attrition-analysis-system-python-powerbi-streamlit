import streamlit as st


# ========================================
# PAGE CONFIG
# ========================================

st.set_page_config(
    page_title="About",
    page_icon="👨‍💻",
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
# TITLE
# ========================================

st.title("👨‍💻 About EAAS")


# ========================================
# PROJECT SECTION
# ========================================

st.markdown(
"""
## 📊 Employee Attrition Analysis System

EAAS is an AI-powered HR analytics platform
designed to analyze employee attrition trends,
predict workforce risks, and provide strategic
business insights.

This project combines:

- Machine Learning
- HR Analytics
- Data Visualization
- Power BI
- Streamlit
- Python Data Science

to create a modern workforce intelligence system.
"""
)


# ========================================
# PROJECT EFFORT
# ========================================

st.markdown("---")

st.markdown(
"""
## 🚀 Project Development Journey

This project was independently designed
and developed with a focus on:

- professional dashboard development
- machine learning integration
- business intelligence
- interactive web applications
- modern UI/UX design
- real-world HR analytics

The system was built using a complete
data analytics workflow:

CSV Dataset
→ Data Cleaning
→ Exploratory Data Analysis
→ Machine Learning
→ Power BI Dashboard
→ Streamlit Deployment
"""
)


# ========================================
# ABOUT YOU
# ========================================

st.markdown("---")

st.markdown(
"""
## 👨‍💻 About the Developer

### Nikhil Kumar Vishwakrma

BCA Student specializing in
Data Science & Artificial Intelligence.

Passionate about:

- Data Analytics
- Machine Learning
- Business Intelligence
- Dashboard Development
- AI-Based Solutions
- HR Analytics Systems

Focused on building practical,
real-world AI and analytics projects.
"""
)


# ========================================
# TRADEMARK SECTION
# ========================================

st.markdown("---")

st.success(
"""
### ™️ EAAS

Employee Attrition Analysis System

Designed & Developed by:

Nikhil Kumar Vishwakrma
(Rameshwaram Vishwakarma)
"""
)


# ========================================
# SIDEBAR
# ========================================

st.sidebar.title("👨‍💻 EAAS")

st.sidebar.info(
"""
About & Project Information
"""
)

st.sidebar.markdown("---")

st.sidebar.success(
"""
EAAS Portfolio Project
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