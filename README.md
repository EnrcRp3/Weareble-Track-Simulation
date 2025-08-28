# 🏃 Wearable Tracker Simulation

Un semplice simulatore di **wearable sportivo** che genera dati fittizi (velocità, battito cardiaco, accelerazione) in tempo reale e li visualizza tramite **Streamlit**.  
Il progetto mostra come si può emulare il comportamento di sensori indossabili per l’analisi delle performance sportive.

---

## ✨ Funzionalità
- Generazione di dati simulati (speed, heart rate, acceleration).
- Possibilità di **aggiungere dati manualmente** con un pulsante.
- Modalità **auto-refresh**: nuovi dati ogni 2 secondi.
- Grafici in tempo reale aggiornati su dashboard Streamlit.
- Conservazione dello storico con `st.session_state`.

---

## 📦 Installazione locale

1. Clona la repo:
   ```bash
   git clone https://github.com/tuo-username/wearable-tracker-simulation.git
   cd wearable-tracker-simulation
   
2. Crea un ambiente virtuale (consigliato):

python -m venv env
source env/bin/activate      # Mac/Linux
env\Scripts\activate         # Windows


3. Installa le dipendenze:

pip install -r requirements.txt


4. Avvia l’app:

streamlit run wearable.py
