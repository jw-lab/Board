from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v*)4a2&brnkza*sdkk-bz7$@--t0ob6$5rs*zrb9v8@9&qsmhm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'parking',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}