import streamlit as st


# ========================================
# PAGE CONFIG
# ========================================

st.set_page_config(
    page_title="Insights",
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

st.title("📊 HR Business Insights")

st.markdown(
"""
### Data-Driven Workforce Intelligence

This section highlights important organizational
patterns discovered from employee data analysis.
"""
)


# ========================================
# INSIGHTS
# ========================================

col1, col2 = st.columns(2)

with col1:

    st.info(
        """
        ### 📌 Overtime Impact

        Employees working overtime show
        significantly higher attrition rates.

        Long-term overtime reduces
        employee retention.
        """
    )

    st.warning(
        """
        ### 💰 Salary Insights

        Employees in lower salary bands
        are more likely to leave.

        Compensation directly impacts
        employee stability.
        """
    )

    st.success(
        """
        ### 😊 Job Satisfaction

        Employees with higher job satisfaction
        remain longer within the organization.

        Employee engagement is critical.
        """
    )

with col2:

    st.error(
        """
        ### 🏢 Department Analysis

        Sales department experiences
        higher employee turnover
        compared to other departments.
        """
    )

    st.info(
        """
        ### 🚗 Travel & Distance

        Employees traveling frequently
        or living farther from work
        show increased attrition trends.
        """
    )

    st.warning(
        """
        ### 📈 Workforce Stability

        Employees staying longer
        in the company generally show
        lower attrition probability.
        """
    )


# ========================================
# FINAL SUMMARY
# ========================================

st.markdown("---")

st.markdown(
"""
## 🎯 Strategic Recommendations

Organizations should focus on:

- improving employee engagement
- reducing excessive overtime
- optimizing compensation structures
- increasing job satisfaction
- improving work-life balance
- strengthening employee retention programs
"""
)


# ========================================
# SIDEBAR
# ========================================

st.sidebar.title("📊 EAAS")

st.sidebar.info(
"""
Business Intelligence Module
"""
)

st.sidebar.markdown("---")

st.sidebar.success(
"""
Insights Engine Running
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