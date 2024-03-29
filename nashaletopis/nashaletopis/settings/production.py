"""Production settings and globals."""


from os import environ

from base import *

from secrets import SECRET_KEY, DB_PASS, EMAIL_PASS


INSTALLED_APPS += ('gunicorn',)
# HOST CONFIGURATION
# See:
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['nashaletopis.ru']
# END HOST CONFIGURATION
COMPRESS_ENABLED = True
# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ksawie@gmail.com'
EMAIL_HOST_PASSWORD = EMAIL_PASS
EMAIL_PORT = 587

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tl
# END EMAIL CONFIGURATION
STATICFILES_DIRS = (
    '/home/maremare/domains/' + SITE_DOMAIN_NAME + '/static/',
)
STATIC_ROOT = '/home/maremare/domains/' + SITE_DOMAIN_NAME + '/staticroot/'
MEDIA_ROOT = '/home/maremare/domains/' + SITE_DOMAIN_NAME + '/media/'

# DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nashaletopis',
        'USER': 'django_login',
        'PASSWORD': DB_PASS,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
# END DATABASE CONFIGURATION


# CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 300
    }
}
# END CACHE CONFIGURATION
