from pathlib import Path
import os
import secrets

# Generate a new SECRET_KEY for development (use only for local development)
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", secrets.token_urlsafe(50))

BASE_DIR = Path(__file__).resolve().parent.parent
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'items',
    'rest_framework',
    'django_celery_results',  # For Celery task results
    'django_celery_beat',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can specify template directories here if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required for admin
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for admin
    'django.contrib.messages.middleware.MessageMiddleware',  # Required for admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATIC_URL = '/static/' 
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
# Celery configurations
# Celery configurations
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672/'  # RabbitMQ
CELERY_ACCEPT_CONTENT = ['json']  # Acceptable content types
CELERY_TASK_SERIALIZER = 'json'   # Serialize tasks as JSON
CELERY_RESULT_BACKEND = 'django-db'  # Store results in Django database
CELERY_CACHE_BACKEND = 'django-cache'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'item_service_db',
        'USER': 'postgres',
        'PASSWORD': '5345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
ALLOWED_HOSTS = ['*']  # Add your hostnames here
DEBUG = True
ROOT_URLCONF = 'item_service.urls'

 


