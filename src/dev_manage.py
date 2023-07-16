#!/usr/bin/env python3

import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ctf_gameserver.web.dev_settings')

    # Importa il modulo socket per configurare l'indirizzo IP e la porta
    import socket
    
    # Modifica l'indirizzo IP e la porta a cui il server si collega
    addr = '0.0.0.0'  # Modifica l'indirizzo IP
    port = 8000  # Modifica la porta

    # Imposta l'indirizzo IP e la porta come variabili d'ambiente per Django
    os.environ["RUNSERVER_ADDR"] = addr
    os.environ["RUNSERVER_PORT"] = str(port)
    
    # Esegui il server Django
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

