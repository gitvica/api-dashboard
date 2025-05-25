import streamlit as st
import requests

def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data["bitcoin"]["usd"]

# Web UI
st.title("Bitcoin Price Tracker")
price = fetch_bitcoin_price()
st.metric(label="Current BTC Price (USD)", value=f"${price}")
