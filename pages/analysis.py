import streamlit as st
import pandas as pd
import plotly.graph_objects as go

add_selectbox = st.sidebar.page_link("homepage.py", label="Dashboard", icon="🏠")
add_selectbox = st.sidebar.page_link("pages/analysis.py", label="Analysis", icon="📈")
add_selectbox = st.sidebar.page_link("pages/settings.py", label="Settings", icon="⚙️")

col1, col2, col3 = st.columns(3)

st.Title("ANALYSIS")
with col1:
    st.text("AAPL DATA")
with col2:
    chart_data = df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df['Date'],
                    open=df['AAPL.Open'], high=df['AAPL.High'],
                    low=df['AAPL.Low'], close=df['AAPL.Close'])
                        )
    st.plotly_chart(fig)