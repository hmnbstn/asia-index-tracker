import streamlit as st
import yfinance as yf
import datetime

# Config Streamlit
st.set_page_config(page_title="AAXJ — MSCI Asia ex Japan", layout="centered")

# Titre & infos
st.title("📈 MSCI Asia ex Japan Tracker")
st.caption("ETF: AAXJ | Powered by Yahoo Finance")

# Télécharger les données
ticker = yf.Ticker("AAXJ")
data = ticker.history(period="6mo")

# Dernier prix et variation
last_price = data["Close"].iloc[-1]
prev_price = data["Close"].iloc[-2]
change = last_price - prev_price
change_pct = (change / prev_price) * 100

# Affichage des données
st.metric(label="Last Price (USD)", value=f"${last_price:.2f}", delta=f"{change:+.2f} ({change_pct:+.2f}%)")

# Courbe de prix
st.line_chart(data["Close"], height=300)

# Horodatage
st.caption(f"Last update: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
