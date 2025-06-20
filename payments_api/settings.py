"""
Django settings for payments_api project.

Generated by 'django-admin startproject' using Django 5.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

import dj_database_url


# Detect if running on Render.com
ON_RENDER = os.getenv('RENDER') is not None

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-!qhu5c_m1r51264uq&=aw+p+ds1i4(utc6eaqoo#nq8d!hn%q*'
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'unsafe-secret-key')
PAYSTACK_SECRET_KEY = os.getenv('PAYSTACK_SECRET_KEY', 'PAYSTACK_SECRET_KEY')
PAYSTACK_PUBLIC_KEY = os.getenv('PAYSTACK_PUBLIC_KEY', 'PAYSTACK_PUBLIC_KEY_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not ON_RENDER

if ON_RENDER:
    # On Render → set allowed hosts (change to your domain or *.onrender.com)
    ALLOWED_HOSTS = ['mastercraft-stage2.onrender.com']
else:
    # Local development
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_spectacular',
    "drf_spectacular_sidecar",
    'rest_framework',
    'payments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'payments_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'payments_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': dj_database_url.config(
#         default='sqlite:///db.sqlite3',  # fallback if DATABASE_URL not set
#         conn_max_age=600
#     )
# }

# Database
DATABASE_URL = os.getenv('DATABASE_URL', os.getenv('PRODUCTION_DATABASE_URL', 'sqlite:///db.sqlite3'))

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'

STATIFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security headers
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Payments API',
    'DESCRIPTION': 'API documentation for Paystack Payments',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}