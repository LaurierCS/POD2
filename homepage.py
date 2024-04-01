import streamlit as st
import pandas as pd
#CONFIG
col1, col2, col3 = st.columns(3)
with col3:
    st.button(label="LOGIN/SIGNUP", help="LOGIN/SIGNUP")


add_selectbox = st.sidebar.page_link("homepage.py", label="Dashboard", icon="🏠")
add_selectbox = st.sidebar.page_link("pages/analysis.py", label="Analysis", icon="📈")
add_selectbox = st.sidebar.page_link("pages/settings.py", label="Settings", icon="⚙️")
st.text("Hi this is where homepage is")
