"""
Django settings for steamboatweb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2i1dklhl1!!_j&p(qjoa$b7(=nhqtrkuoj2g(hl*=%+*vn$cr='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'projects',
    'contact',
    'about',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'steamboatweb.urls'

WSGI_APPLICATION = 'steamboatweb.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'amber@steamboatlabs.com'
EMAIL_HOST_PASSWORD = 'funnyllama'
EMAIL_USE_TLS = True

CONTACT_EMAILS = ['amber@steamboatlabs.com']


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
) 

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

ADMINS = (('Sam', 'sam@steamboatlabs.com'), ('Amber', 'amber@steamboatlabs.com'))

# Allow all host hosts/domain names for this site
ALLOWED_HOSTS = ['*']

# Parse database configuration from $DATABASE_URL	
import dj_database_url

DATABASES = {'default': dj_database_url.config()}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'HTTPS')

# try to load local_settings.py if it exists
try:
    from local_settings import *
except Exception as e:
    pass

#S3 storage
# from S3 import CallingFormat
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = 'AKIAI36BTSMMNYWRG2VA'

AWS_SECRET_ACCESS_KEY = '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'

AWS_STORAGE_BUCKET_NAME = 'steamboatweb'

# AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN