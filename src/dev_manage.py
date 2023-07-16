#!/usr/bin/env python3

import os
import sys


from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ctf_gameserver.web.dev_settings')
    execute_from_command_line(['dev_manage.py', 'runserver', '0.0.0.0:8000'])
    