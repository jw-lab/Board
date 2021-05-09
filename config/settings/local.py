from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v*)4a2&brnkza*sdkk-bz7$@--t0ob6$5rs*zrb9v8@9&qsmhm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}