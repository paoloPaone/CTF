#!/usr/bin/env python3

import os
import sys


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ctf_gameserver.web.dev_settings')
    
    # Modifica l'indirizzo IP e la porta a cui il server si collega
    # da 127.0.0.1:8000 a 0.0.0.0:8000
    from django.core.management import execute_from_command_line
    from django.core.servers.basehttp import get_internal_wsgi_application
    from django.core.management.commands.runserver import Command as runserver
    

    import socket
    
    # Modifica l'indirizzo IP e la porta a cui il server si collega
    addr = '0.0.0.0'  # Modifica l'indirizzo IP
    port = 8000  # Modifica la porta

    # Imposta l'indirizzo IP e la porta come variabili d'ambiente per Django
    os.environ["RUNSERVER_ADDR"] = addr
    os.environ["RUNSERVER_PORT"] = str(port)
    
    runserver.default_addr = '0.0.0.0'
    runserver.default_port = '8000'
    runserver.default_ipv6 = False
    
    execute_from_command_line(sys.argv)
