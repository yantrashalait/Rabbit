import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ')(@e9d(j)luh(4*hbp1qc_=ncaev#*(+$d_dmgl@4uxdk6t_hd'

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rabbit',
        'USER': 'postgres',
        'PASSWORD': 'rajiv123',
        'HOST': '',
        'PORT': '',
    }
}

from .settings import INSTALLED_APPS
INSTALLED_APPS +=['item']


SEND_ACTIVATION_EMAIL = True
ACCOUNT_ACTIVATION_DAYS = 30
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'rajeev.nepali1001@gmail.com'
EMAIL_HOST_PASSWORD = 'beinghuman1001001'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# uncomment below in development
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# use in deployment
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
