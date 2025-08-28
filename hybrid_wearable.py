import random
import pandas as pd
import streamlit as st
import time

st.set_page_config(page_title="Wearable Tracker Simulation", layout="wide")
st.title("🏃 Wearable Tracker Simulation")

# Inizializza session_state se vuoto
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(columns=["timestamp", "speed", "heart_rate", "acceleration"])

# Funzione per aggiungere un nuovo dato simulato
def add_new_data():
    new_row = {
        "timestamp": pd.Timestamp.now(),
        "speed": round(random.uniform(5, 25), 2),         # km/h
        "heart_rate": random.randint(90, 190),            # bpm
        "acceleration": round(random.uniform(-3, 3), 2)   # m/s^2
    }
    st.session_state["data"] = pd.concat(
        [st.session_state["data"], pd.DataFrame([new_row])],
        ignore_index=True
    )

# 🔹 Pulsante per aggiungere dati manualmente
if st.button("➕ Aggiungi nuovo dato"):
    add_new_data()

# 🔹 Auto-refresh ogni 2 secondi
auto_refresh = st.sidebar.checkbox("Auto-refresh attivo", value=True)

if auto_refresh:
    # usa un contatore in session_state invece dei query_params
    if "counter" not in st.session_state:
        st.session_state["counter"] = 0
    st.session_state["counter"] += 1

    if st.session_state["counter"] % 2 == 0:  # ogni 2 cicli = 2 secondi
        add_new_data()
    time.sleep(2)
    st.experimental_rerun()

# 🔹 Mostra i grafici
if not st.session_state["data"].empty:
    df = st.session_state["data"].set_index("timestamp")
    st.subheader("Andamento velocità e battito cardiaco")
    st.line_chart(df[["speed", "heart_rate"]])
    st.subheader("Andamento accelerazione")
    st.line_chart(df[["acceleration"]])
else:
    st.info("Clicca il pulsante o abilita l'auto-refresh per generare dati.")
