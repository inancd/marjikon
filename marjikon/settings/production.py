from .base import *
from dotenv import load_dotenv
import os
load_dotenv()


ALLOWED_HOSTS = ['marjikon.com', 'www.marjikon.com']
STATIC_ROOT = BASE_DIR / 'static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}