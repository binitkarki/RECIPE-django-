import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS=[os.environ.get('RENDER_EXTERNAL_HOSTNAME')]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('RENDER_EXTERNAL_HOSTNAME')]


DEBUG=False
SECRET_KEY=os.environ.get('SECRET_KEY')

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",          
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
CORS_ALLOWED_ORIGINS = [
    "https://recipe-react-mwlx.onrender.com"                  
]

CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
]
STORAGES={
    "default":{
        "BACKEND":"django.core.files.storage.FileSystemStorage",
    },
    "staticfiles":{
        "BACKEND":"whitenoise.storage.CompressedStaticFilesStorage",
    },
}

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
