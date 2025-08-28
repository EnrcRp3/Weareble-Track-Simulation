import time
import random
import pandas as pd
import streamlit as st

# Inizializza DataFrame vuoto
data = pd.DataFrame(columns=["timestamp", "speed", "heart_rate", "acceleration"])

st.title("🏃 Wearable Tracker Simulation")

# Placeholder per grafici
placeholder = st.empty()

# Genera dati simulati (con loop controllato, max 100 iterazioni)
for i in range(50):
    new_row = {
        "timestamp": pd.Timestamp.now(),
        "speed": round(random.uniform(5, 25), 2),         # km/h
        "heart_rate": random.randint(90, 190),            # bpm
        "acceleration": round(random.uniform(-3, 3), 2)   # m/s^2
    }
    # Concatenazione sicura
    new_row_df = pd.DataFrame([new_row])
    data = pd.concat([data, new_row_df], ignore_index=True)

    # Imposta indice temporale
    data = data.set_index("timestamp")

    with placeholder.container():
        st.line_chart(data[["speed", "heart_rate"]])
        st.line_chart(data[["acceleration"]])

    time.sleep(0.5)
