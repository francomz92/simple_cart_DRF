from datetime import timedelta

from django.conf import settings

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=20),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'SIGNING_KEY': settings.SECRET_KEY,
    'ALGORITHM': 'HS256',
    'AUTH_HEADER_TYPE': ('Bearer', ),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}