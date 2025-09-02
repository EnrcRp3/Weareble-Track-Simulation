import streamlit as st
import pandas as pd
import json
import paho.mqtt.client as mqtt

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

# Setup MQTT client (solo una volta)
if "mqtt_client" not in st.session_state:
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.subscribe(TOPIC)
    client.loop_start()
    st.session_state["mqtt_client"] = client

# Refresh UI
st.markdown("### Dati in tempo reale")
if not st.session_state["data"].empty:
    df = st.session_state["data"].set_index("timestamp")
    st.line_chart(df[["speed", "heart_rate"]])
    st.line_chart(df[["acceleration"]])
else:
    st.info("⏳ In attesa di dati dal wearable (publisher MQTT)...")

# Forza refresh automatico ogni 5 secondi
st.autorefresh(interval=5000, key="mqtt-refresh")
