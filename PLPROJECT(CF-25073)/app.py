import streamlit as st
import dataloader
import simulator
import visualizer
import predictor

# Page Configuration
st.set_page_config(page_title="Financial Simulator", layout="wide")

# Main Title
st.title("🚀 Financial Simulator")

# Load data
df = dataloader.load_data()

# Navigation Sidebar
# --- Professional Sidebar Navigation ---
st.sidebar.header("🧭 Navigation Hub")

menu = st.sidebar.selectbox(
    "Choose an Analysis Module:", 
    [
        "🏠 Home", 
        "📈 Profitability Calculator", 
        "⏳ Cash Runway Estimator", 
        "🔮 Revenue Predictor", 
        "🏢 Company Health Dashboard"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Developed by: Neha Batool | Roll No: CF-073")
st.sidebar.success("Status: System Ready ✅")

# --- Routing Logic ---
if menu == "🏠 Home":
    st.write("Welcome to the Financial Command Center. Use the sidebar to explore performance metrics, risk assessments, and future revenue projections.")

elif menu == "📈 Profitability Calculator":
    simulator.show_profitability(df)

elif menu == "⏳ Cash Runway Estimator":
    simulator.show_cash_runway(df)

elif menu == "🔮 Revenue Predictor":
    simulator.show_predictor(df)

elif menu == "🏢 Company Health Dashboard":
    st.header("🏢 Overall Company Health")
    risk, color, score = simulator.get_health_metrics(df)
    
    st.subheader(f"Risk Level: {risk}")
    st.progress(score / 100)
    
    st.write("### Health Breakdown")
    st.markdown(f"**Overall Health Score:** <span style='color:{color}'>{score}/100</span>", unsafe_allow_html=True)
    st.write("This score is calculated based on current Net Profit Margins.")
