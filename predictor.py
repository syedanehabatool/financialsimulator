import pandas as pd

def get_revenue_prediction(df):
    df = df.sort_values('Year')
    growth_rates = df['Total Revenue'].pct_change().dropna()
    avg_growth = growth_rates.mean()
    last_revenue = df['Total Revenue'].iloc[-1]
    predicted_revenue = last_revenue * (1 + avg_growth)
    return predicted_revenue, avg_growth
