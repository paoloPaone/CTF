import json

# Definisci le informazioni essenziali
service_name = "fitty-fit"
service_slug = "fittyfit"
num_teams = 2  # Sostituisci con il numero desiderato di team

# Crea una lista vuota per i dati dei team
teams_data = []

# Genera i dati dei team
for i in range(1, num_teams + 1):
    team_data = {
        "model": "auth.user",
        "pk": i+1,
        "fields": {
            "password": "pbkdf2_sha256$36000$kHAF2GkRGCyG$qm+7EyJr0b8E9VbQWp3ZtfxaV0A5wIJSV/ABWEML6II=",
            "last_login": None,
            "is_superuser": False,
            "username": f"Team{i}",
            "first_name": f"team{i}",
            "last_name": f"team{i}",
            "email": "",
            "is_staff": False,
            "is_active": True,
            "date_joined": "2023-06-22T18:21:28.622Z",
            "groups": [],
            "user_permissions": [],
        },
    }
    team_data2 = {
        "model": "registration.team",
        "pk": i+1,
        "fields": {
            "net_number": i,
            "informal_email": f"team{i}@example.org",
            "image": "",
            "affiliation": "",
            "country": "IT",
            "nop_team": False,
        },
    }
    teams_data.append(team_data)
    teams_data.append(team_data2)

# Definisci i dati per il servizio e il game control
service_data = {
    "model": "scoring.service",
    "pk": 1,
    "fields": {
        "name": service_name,
        "slug": service_slug,
    },
}

game_control_data = {
    "model": "scoring.gamecontrol",
    "pk": 1,
    "fields": {
        "competition_name": "My CTF (A/D)",
        "tick_duration": 180,
        "valid_ticks": 5,
        "current_tick": -1,
        "flag_prefix": "U29tZSBzdHJpbmcgZXhh",
        "registration_open": False,
        "services_public": "$SERVICE_PUBLIC_TIME",
        "start": "$START_TIME",
        "end": "$END_TIME",
    },
}

# Crea la lista finale dei dati
data = teams_data + [service_data, game_control_data]

# Serializza i dati in formato JSON
json_data = json.dumps(data, indent=4)

# Scrivi i dati JSON su un file
with open("master.json", "w") as json_file:
    json_file.write(json_data)

print("File JSON generato con successo!")
