import random
import pandas as pd
import streamlit as st

st.title("🏃 Wearable Tracker Simulation")

# Inizializza session_state se vuoto
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(columns=["timestamp", "speed", "heart_rate", "acceleration"])

# Genera nuovo dato quando clicchi il pulsante
if st.button("Aggiungi nuovo dato"):
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

# Prepara dati per grafico
if not st.session_state["data"].empty:
    df = st.session_state["data"].set_index("timestamp")

    st.line_chart(df[["speed", "heart_rate"]])
    st.line_chart(df[["acceleration"]])
else:
    st.info("Clicca il pulsante per generare i primi dati.")
