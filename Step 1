import time
import random
import pandas as pd
import streamlit as st

# Inizializza DataFrame vuoto
data = pd.DataFrame(columns=["timestamp", "speed", "heart_rate", "acceleration"])

st.title("🏃 Wearable Tracker Simulation")

# Simulatore
placeholder = st.empty()

# Loop di simulazione (streaming)
for i in range(100):
    new_row = {
        "timestamp": pd.Timestamp.now(),
        "speed": round(random.uniform(5, 25), 2),         # km/h
        "heart_rate": random.randint(90, 190),            # bpm
        "acceleration": round(random.uniform(-3, 3), 2)   # m/s^2
    }
    data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)

    with placeholder.container():
        st.line_chart(data.set_index("timestamp")[["speed", "heart_rate"]])
        st.line_chart(data.set_index("timestamp")[["acceleration"]])

    time.sleep(0.5)
