import streamlit as st
import pandas as pd
import plotly.graph_objects as go

add_selectbox = st.sidebar.page_link("homepage.py", label="Dashboard", icon="🏠")
add_selectbox = st.sidebar.page_link("pages/analysis.py", label="Analysis", icon="📈")
add_selectbox = st.sidebar.page_link("pages/settings.py", label="Settings", icon="⚙️")


tab1, tab2 = st.tabs(["Financials", "Earnings"])
chart_data = df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

with tab1:
   col1, col2 = st.columns(2)
   with col1:
    st.header("AAPL data")
    with col2:
      st.metric("Last Close", "171.48", "-1.83 (1.06%)")
   fig = go.Figure()
   fig.add_trace(go.Candlestick(x=df['Date'],
                        open=df['AAPL.Open'], high=df['AAPL.High'],
                        low=df['AAPL.Low'], close=df['AAPL.Close'])
                            )
   st.plotly_chart(fig)
   


with tab2:
   st.header("Earnings")
   earnings_data = pd.read_csv("./aapldata.csv")
   st.table(earnings_data)