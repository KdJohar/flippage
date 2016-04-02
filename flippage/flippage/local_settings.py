import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

STATIC_ROOT = os.path.join(BASE_DIR, "../static")

MEDIA_ROOT = os.path.join(BASE_DIR, "../media")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'flippage',
        'USER': 'root',
        'PASSWORD': 'calloser',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
