import streamlit as st
import pandas as pd
import streamlit_shadcn_ui as ui
import json
import requests
#CONFIG

#initialize top 3 gainers
top1 = 0
top2 = 0
top3 = 0

h_perc = []
l_perc = []
#sample data
with open('./query.json', 'r') as f:
  data = json.load(f)

#url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=9M4TJBS45SVG391Z'
#r = requests.get(url)
#stocks_data = r.json()
stocks_data = data

top_gainers = stocks_data["top_gainers"]
top_losers = stocks_data["top_losers"]

for x in range(len(top_gainers)):
    h_perc.append(float(top_gainers[x]["change_percentage"].rstrip("%")))

for x in range(len(top_losers)):
    l_perc.append(float(top_losers[x]["change_percentage"].rstrip("%")))

#Get biggest winner
def getBiggest(arr, topind):
     top = arr[topind]["ticker"]
     topprice = arr[topind]["price"]
     topchange = arr[topind]["change_percentage"]
     toppricechange = arr[topind]["change_amount"]
     return top, topprice, topchange, toppricechange

#Get biggest gainer
top1, top1price, top1change, top1pricechange = getBiggest(top_gainers, h_perc.index(max(h_perc)))
h_perc.pop(h_perc.index(max(h_perc)))
#Get 2nd biggest gainer, add 1 to make up for popped values
top2, top2price, top2change, top2pricechange = getBiggest(top_gainers, h_perc.index(max(h_perc)) + 1)

h_perc.pop(h_perc.index(max(h_perc)))
#Get 3rd biggest gainer, add 2 to make up for popped values
top3, top3price, top3change, top3pricechange = getBiggest(top_gainers, h_perc.index(max(h_perc)) + 2)

#get biggest loser
bot1, bot1price, bot1change, bot1pricechange = getBiggest(top_losers, l_perc.index(min(l_perc)))

l_perc.pop(l_perc.index(min(l_perc)))

#get 2nd biggest loser
bot2, bot2price, bot2change, bot2pricechange = getBiggest(top_losers, l_perc.index(min(l_perc)) + 1)

l_perc.pop(l_perc.index(min(l_perc)))

#get 3rd biggest loser
bot3, bot3price, bot3change, bot3pricechange = getBiggest(top_losers, l_perc.index(min(l_perc)) + 2)


#initialize sidebar
add_selectbox = st.sidebar.page_link("homepage.py", label="Dashboard", icon="🏠")
add_selectbox = st.sidebar.page_link("pages/analysis.py", label="Analysis", icon="📈")
add_selectbox = st.sidebar.page_link("pages/settings.py", label="Settings", icon="⚙️")
cols2 = st.columns(5)
with cols2[4]:
     st.button(label="LOGIN/SIGNUP", help="LOGIN/SIGNUP")
st.header("TOP GAINERS")
gainercolumn = st.columns(3)

with gainercolumn[0]:
    ui.metric_card(title=top1, content=top1price, description="+" + top1pricechange + " (+" + top1change + ")", key="card1")
with gainercolumn[1]:
     ui.metric_card(title=top2, content=top2price, description="+" + top2pricechange + " (+" + top2change + ")", key="card2")
with gainercolumn[2]:
     ui.metric_card(title=top3, content=top3price, description="+" + top3pricechange + " (+" + top3change + ")", key="card3")

st.dataframe(top_gainers, use_container_width=True)
st.header("TOP LOSERS")
losercolumn = st.columns(3)

with losercolumn[0]:
    ui.metric_card(title=bot1, content=bot1price, description=bot1pricechange + " (" + bot1change + ")", key="lcard1")
with losercolumn[1]:
     ui.metric_card(title=bot2, content=bot2price, description= bot2pricechange + " (" + bot2change + ")", key="lcard2")
with losercolumn[2]:
     ui.metric_card(title=bot3, content=bot3price, description=bot3pricechange + " (" + bot3change + ")", key="lcard3")

st.dataframe(top_losers, use_container_width=True)