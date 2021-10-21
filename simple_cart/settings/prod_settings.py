from .base_settings import *
from corsheaders.defaults import default_headers, default_methods

SECRET_KEY = 'django-insecure-e5o5%bo%8i4h5(ez386nfjjpap(ju5)$0t%#z6!7lwo##xra-u'

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'learning_django_rest',
        'USERNAME': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CORS_ALLOW_ALL_ORIGIN = False

CORS_ALLOWED_ORIGINS = []

CORS_ALLOW_METHODS = list(default_methods)

CORS_ALLOW_HEADERS = list(default_headers)

CORS_PREFLIGHT_MAX_AGE = 60 * 60 * 24  # 60 seconds * 60 minutes * 24 hours

CSRF_TRUSTED_ORIGINS = []

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 465
# EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
