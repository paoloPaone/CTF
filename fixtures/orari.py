import json
import datetime

# Leggi il file JSON
with open('master.json', 'r') as file:
    data = json.load(file)

# Calcola gli orari desiderati
current_time = datetime.datetime.now()
service_public_time = current_time + datetime.timedelta(minutes=2)
start_time = current_time + datetime.timedelta(minutes=5)
end_time = start_time + datetime.timedelta(hours=1)

# Sostituisci le variabili JSON con i valori calcolati
data["fields"]["services_public"] = service_public_time.isoformat()
data["fields"]["start"] = start_time.isoformat()
data["fields"]["end"] = end_time.isoformat()

# Scrivi il file JSON aggiornato
with open('config.json', 'w') as file:
    json.dump(data, file, indent=4)
