from .base import *
from dotenv import load_dotenv
import os
load_dotenv()


ALLOWED_HOSTS = ['marjikon.com', 'www.marjikon.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '',
    }
}