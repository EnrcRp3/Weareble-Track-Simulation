import streamlit as st
import pandas as pd
import json
import paho.mqtt.client as mqtt
import time

# Config MQTT
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "wearable/athlete1"

st.set_page_config(page_title="Wearable Tracker Dashboard", layout="wide")
st.title("📡 Wearable Tracker Dashboard (MQTT)")

# Inizializza session_state
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(columns=["timestamp", "speed", "heart_rate", "acceleration"])

# Funzione callback MQTT
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        new_row = {
            "timestamp": pd.to_datetime(payload["timestamp"], unit="s"),
            "speed": payload["speed"],
            "heart_rate": payload["heart_rate"],
            "acceleration": payload["acceleration"]
        }
        st.session_state["data"] = pd.concat(
            [st.session_state["data"], pd.DataFrame([new_row])],
            ignore_index=True
        )
    except Exception as e:
        st.error(f"Errore parsing messaggio: {e}")

# Setup MQTT client (solo una volta)
if "mqtt_client" not in st.session_state:
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.subscribe(TOPIC)
    client.loop_start()
    st.session_state["mqtt_client"] = client

# UI placeholder
placeholder = st.empty()

with placeholder.container():
    if not st.session_state["data"].empty:
        df = st.session_state["data"].set_index("timestamp")
        st.subheader("Andamento velocità e battito cardiaco")
        st.line_chart(df[["speed", "heart_rate"]])
        st.subheader("Andamento accelerazione")
        st.line_chart(df[["acceleration"]])
        st.write("Ultimo dato ricevuto:", st.session_state["data"].iloc[-1].to_dict())
    else:
        st.info("⏳ In attesa di dati dal wearable (publisher MQTT)...")

# Aspetta 5 secondi e ricarica lo script
time.sleep(5)
st.rerun()
