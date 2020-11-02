from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {        
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'personalweb',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}



STATIC_URL = '/static/'
STATICFILES_DIRS = [
    "static",
]

MEDIA_ROOT = 'media'

MEDIA_URL = '/media/'

