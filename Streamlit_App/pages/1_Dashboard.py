import streamlit as st

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

st.markdown(
"""
<div class="page-enter-animation">
""",
unsafe_allow_html=True
)

st.title("📊 EAAS Dashboards")

st.subheader("Executive Overview")
st.image(
    r"X:\CODES\PROJECTS\NXDAXEAAS01_Employee_Attrition_Analytics_System_050726\Streamlit_App\assets\images\Executive_Overview.png",
    use_container_width=True
)

st.subheader("Attrition Analysis")
st.image(
    r"X:\CODES\PROJECTS\NXDAXEAAS01_Employee_Attrition_Analytics_System_050726\Streamlit_App\assets\images\Attrition_Analysis.png",
    use_container_width=True
)

st.subheader("Salary & Satisfaction")
st.image(
    r"X:\CODES\PROJECTS\NXDAXEAAS01_Employee_Attrition_Analytics_System_050726\Streamlit_App\assets\images\Salary_&_Satisfaction.png",
    use_container_width=True
)

st.subheader("Employee Risk Insights")
st.image(
    r"X:\CODES\PROJECTS\NXDAXEAAS01_Employee_Attrition_Analytics_System_050726\Streamlit_App\assets\images\Employee_Risk_Insights.png",
    use_container_width=True
)
st.sidebar.title("EAAS")
st.sidebar.info("Employee Attrition Analysis System")
st.markdown("---")
st.caption('''Developed by Nikhil Kumar Vishwakrma
           (Rameshwaram Vishwakarma)''')

st.markdown(
"""
</div>
""",
unsafe_allow_html=True
)