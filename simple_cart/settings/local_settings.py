from .base_settings import *
from corsheaders.defaults import default_methods, default_headers

SECRET_KEY = 'django-insecure-e5o5%bo%8i4h5(ez386nfjjpap(ju5)$0t%#z6!7lwo##xra-u'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        #   'ENGINE': 'django.db.backends.mysql',
        #   'HOST': 'localhost',
        #   'PORT': '3306',
        #   'NAME': '',
        #   'USER': '',
        #   'PASSWORD': '',
    }
}

# Cors settings

CORS_ALLOW_ALL_ORIGIN = False

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:8000',
#     'http://127.0.0.1:8000',
# ]

CORS_ALLOW_METHODS = list(default_methods)

CORS_ALLOW_HEADERS = list(default_headers)

CORS_PREFLIGHT_MAX_AGE = 3600

# CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    'localhost:8000',
    '127.0.0.1:8000',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_USE_TLS = True
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = 'your_mail_server'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_HOST_USER = 'your_email'
EMAIL_PORT = 465
# EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER