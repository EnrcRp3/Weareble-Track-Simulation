import time
import random
import json
import paho.mqtt.client as mqtt

# Configurazione broker pubblico (Mosquitto)
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "wearable/athlete1"

# Crea client
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("📡 Connessione al broker MQTT...")

while True:
    # Simula dati sensore
    payload = {
        "timestamp": time.time(),
        "speed": round(random.uniform(5, 25), 2),
        "heart_rate": random.randint(90, 190),
        "acceleration": round(random.uniform(-3, 3), 2)
    }

    # Converte in JSON e invia
    client.publish(TOPIC, json.dumps(payload))
    print("Dati inviati:", payload)

    time.sleep(2)  # ogni 2 secondi
