import streamlit as st
import visualizer
import predictor

def show_profitability(df):
    st.header("📈 Profitability Calculator")
    df['Profit Margin (%)'] = (df['Net Income'] / df['Total Revenue']) * 100
    visualizer.create_colorful_chart(df, 'Year', 'Profit Margin (%)', "Net Profit Margin Trend")
    st.dataframe(df[['Year', 'Net Income', 'Total Revenue', 'Profit Margin (%)']])

def show_cash_runway(df):
    st.header("💰 Cash Runway Estimator")
    visualizer.create_colorful_chart(df, 'Year', 'Net Income', "Net Income Performance")

def show_predictor(df):
    st.header("🔮 Revenue Predictor")
    prediction, growth_rate = predictor.get_revenue_prediction(df)
    st.metric(label="Predicted Revenue", value=f"${prediction:,.0f}")
    st.write(f"Based on an average historical growth rate of {growth_rate:.2%}")

def get_health_metrics(df):
    """Calculates overall company health and risk."""
    latest = df.iloc[-1]
    
    # Ensure columns exist (check your CSV column names!)
    net_income = latest['Net Income']
    total_rev = latest['Total Revenue']
    
    margin = (net_income / total_rev) * 100
    
    if margin > 20:
        risk, color, score = "Low Risk 🟢", "green", 90
    elif margin > 10:
        risk, color, score = "Medium Risk 🟡", "orange", 60
    else:
        risk, color, score = "High Risk 🔴", "red", 30
        
    return risk, color, score
