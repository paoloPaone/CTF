"""
Django and project specific settings for usage during development.
Everything should be ready-to-go for a common development environment, but you may of course tweak some
options.
"""

# pylint: disable=wildcard-import, unused-wildcard-import
from .base_settings import *








CSP_POLICIES = {
    'base-uri': ["'self'"],
    'connect-src': ["'self'"],
    'form-action': ["'self'"],
    'object-src': ["'none'"],
    'script-src': ["'self'", "'unsafe-inline'"],  # Aggiungi 'unsafe-inline' qui
    'style-src': ["'self'"]
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev-db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'ctf-gameserver.web@localhost'

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
TEAM_DOWNLOADS_ROOT = os.path.join(BASE_DIR, 'team_downloads')

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

SECRET_KEY = 'OnlySuitableForDevelopment'    # nosec

TIME_ZONE = 'UTC'
FIRST_DAY_OF_WEEK = 1


ALLOWED_HOSTS = ['0.0.0.0','172.17.0.2','127.0.0.1','localhost']

DEBUG = True
INTERNAL_IPS = ['127.0.0.1']



GRAYLOG_SEARCH_URL = 'http://localhost:9000/search'
