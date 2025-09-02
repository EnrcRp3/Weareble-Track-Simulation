import paho.mqtt.client as mqtt
import json

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "wearable/enrico/test"  # 👈 stesso del publisher

def on_connect(client, userdata, flags, rc):
    print("✅ Connesso al broker con codice:", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print("📥 Messaggio ricevuto:", payload)
    except Exception as e:
        print("Errore parsing:", e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()
