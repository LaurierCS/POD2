import streamlit as st
import pandas as pd
import streamlit_shadcn_ui as ui
#CONFIG
st.button(label="LOGIN/SIGNUP", help="LOGIN/SIGNUP")
cols = st.columns(3)

with cols[0]:
    ui.metric_card(title="S&P 500", content="5,197.93", description="-58.84 (-1.12%)", key="card1")
with cols[1]:
     ui.metric_card(title="DOW 30", content="39,077.71", description="-489.14 (-1.24%)", key="card2")
with cols[2]:
     ui.metric_card(title="NASDAQ", content="16146.29", description="-251.33 (-1.54%)", key="card3")



add_selectbox = st.sidebar.page_link("homepage.py", label="Dashboard", icon="🏠")
add_selectbox = st.sidebar.page_link("pages/analysis.py", label="Analysis", icon="📈")
add_selectbox = st.sidebar.page_link("pages/settings.py", label="Settings", icon="⚙️")
st.text("Hi this is where homepage is")
choice = ui.select(options=["AAPL","MSFT", "YTSL", "GOOG"])
