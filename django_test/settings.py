"""
Django settings for django_test project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from decouple import config
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '=5rmg9_wgb4iz8)+ro^xw63^80!6mbca*8lb-mh9d8jg7y!jfj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dawa-test.herokuapp.com', 'localhost']


# Application definition

INSTALLED_APPS = (
    'import_export',
    'dashboard',
    'users',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'django.contrib.sites',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'django_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'django_test.wsgi.application'


##Added import_export settings code
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'),)
}

if os.environ.get('IMPORT_EXPORT_TEST_TYPE') == 'postgres':
    IMPORT_EXPORT_USE_TRANSACTIONS = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': os.environ.get('IMPORT_EXPORT_POSTGRESQL_USER'),
            'PASSWORD': os.environ.get('IMPORT_EXPORT_POSTGRESQL_PASSWORD'),
            'HOST': 'localhost',
            'PORT': 5432
        }
    }
elif os.environ.get('IMPORT_EXPORT_TEST_TYPE') == 'mysql-innodb':
    IMPORT_EXPORT_USE_TRANSACTIONS = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'TEST_NAME': 'import_export_test',
            'USER': os.environ.get('IMPORT_EXPORT_MYSQL_USER', 'root'),
            'OPTIONS': {
               'init_command': 'SET storage_engine=INNODB',
            }
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.path.dirname(__file__), 'database.db'),
        }
    }


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases



db_from_env = dj_database_url.config(conn_max_age=500)
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


LOGIN_REDIRECT_URL = '/dashboard/'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
