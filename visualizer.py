import streamlit as st
import plotly.express as px

def create_colorful_chart(df, x_col, y_col, title):
    fig = px.line(df, x=x_col, y=y_col, title=title, markers=True)
    fig.update_traces(line_color='#FF4B4B', line_width=4)
    fig.update_layout(template="plotly_dark", title_font_size=24)
    st.plotly_chart(fig, use_container_width=True)
