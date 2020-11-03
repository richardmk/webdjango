from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

import dj_database_url

DATABASES = {
    'default' : dj_database_url.config(
        default = config('DATABASE_URL')
    )
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')