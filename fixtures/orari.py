import json
import datetime
import pytz  # Importa il modulo pytz per gestire il fuso orario

# Leggi il file JSON
with open('master.json', 'r') as file:
    data = json.load(file)

# Ottieni il fuso orario "Europe/Rome"
rome_timezone = pytz.timezone("Europe/Rome")

# Calcola gli orari desiderati in base al fuso orario
current_time = datetime.datetime.now(rome_timezone)
service_public_time = current_time + datetime.timedelta(minutes=2)
start_time = current_time + datetime.timedelta(minutes=5)
end_time = start_time + datetime.timedelta(hours=1)

# Rimuovi i secondi e i microsecondi
service_public_time = service_public_time.replace(second=0)
start_time = start_time.replace(second=0)
end_time = end_time.replace(second=0)

# Sostituisci le variabili JSON con i valori calcolati in formato ISO 8601
for item in data:
    if item.get("model") == "scoring.gamecontrol":
        item["fields"]["services_public"] = service_public_time.isoformat()
        item["fields"]["start"] = start_time.isoformat()
        item["fields"]["end"] = end_time.isoformat()

# Scrivi il file JSON aggiornato
with open('master.json', 'w') as file:
    json.dump(data, file, indent=4)
