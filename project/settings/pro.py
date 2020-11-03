from .base import *

from decouple import config
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ['richardmejia.herokuapp.com', '127.0.0.1']

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR,'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')