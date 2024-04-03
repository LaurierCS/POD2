import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from stocks.alphavantage import Model

add_selectbox = st.sidebar.page_link("homepage.py", label="Dashboard", icon="🏠")
add_selectbox = st.sidebar.page_link("pages/analysis.py", label="Analysis", icon="📈")
add_selectbox = st.sidebar.page_link("pages/settings.py", label="Settings", icon="⚙️")

symbol = ''
months = 0
valid = False

def search():
   global symbol, months, valid
   valid = False
   model = Model()
   symbol = text_input.upper()
   months = number_input
   dates, forecast_values = model.predict(symbol, months) 
   if dates != 400 and symbol != '':
      valid = True
      return dates, forecast_values
   else:
      st.error("Symbol not found. Please enter a valid stock symbol")
      return [], []


text_input = st.text_input("Enter the stock symbol here:")
number_input = st.number_input("Enter the number of months to predict:", min_value=1, max_value=24, step=1)
button_clicked = st.button("Create prediction")

if button_clicked:
    dates, forecast_values = search()
    if valid:
        tab1, tab2 = st.tabs(["Forecast", "Predictions"])
        chart_data = df = pd.read_csv(f'./stocks\{symbol}.csv')

        with tab1:
            col1, col2 = st.columns(2)
            with col1:
               st.header(f"{symbol} Forecast for the Next {months} Months")
               fig = go.Figure()
               fig.add_trace(go.Scatter(x=dates, y=forecast_values['open'], mode='lines', name='Open Price'))
               min_open = forecast_values['open'].min()
               max_open = forecast_values['open'].max()
               y_range = [min_open * 0.9, max_open * 1.1]  
               fig.update_layout(yaxis_range=y_range)
               st.plotly_chart(fig)

    if valid:
        with tab2:
            st.header("Data")
            earnings_data = pd.read_csv(f"./stocks\{symbol}.csv")  
            st.table(earnings_data)