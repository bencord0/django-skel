"""Common settings and globals."""


from datetime import timedelta
from os import environ
from os.path import abspath, basename, dirname, join, normpath
import random
from sys import path

from djcelery import setup_loader
truthy = ['True', 'true', 'Y', 'y', '1']

import dj_database_url
from memcacheify import memcacheify


########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = environ.get('DEBUG', 'False') in truthy

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_VIA_CONSOLE = 'django.core.mail.backends.console.EmailBackend'
EMAIL_VIA_SMTP = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = EMAIL_VIA_CONSOLE if DEBUG else EMAIL_VIA_SMTP
########## END EMAIL CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
# Set the environment ADMINS variable from a comma separated list of
# name:<email@domain> pairs.
ADMINS = ((name_email.strip().split(':')) for name_email in environ.get('ADMINS', '').split(','))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# https://github.com/kennethreitz/dj-database-url
DATABASES = {'default': dj_database_url.config(
    default='sqlite:///{}'.format(normpath(join(DJANGO_ROOT, 'default.db'))))}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# https://github.com/rdegges/django-heroku-memcacheify
# Will use local memory caching as a backup
CACHES = memcacheify()
########## END CACHE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = environ.get('TIME_ZONE', 'Europe/London')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = environ.get('LANGUAGE_CODE', 'en-gb')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = int(environ.get('SITE_ID', '1'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = environ.get('USE_I18N', 'True') in truthy

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = environ.get('USE_L10N', 'True') in truthy
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))
MEDIA_ROOT = environ.get('MEDIA_ROOT', MEDIA_ROOT)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = environ.get('MEDIA_URL', '/media/')
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# See: https://github.com/kennethreitz/dj-static/blob/master/README.rst
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))
STATIC_ROOT = environ.get('STATIC_ROOT', STATIC_ROOT)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = environ.get('STATIC_URL', '/static/')

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
#    normpath(join(DJANGO_ROOT, 'assets')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = environ.get('SECRET_KEY', "".join([random.choice(
               "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
             ) for i in range(50)]))
if not environ.get('SECRET_KEY'):
    print("SECRET_KEY is not set: Using a temporary value instead")
    print("SECRET_KEY: {}".format(SECRET_KEY))
########## END SECRET CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(DJANGO_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # Use GZip compression to reduce bandwidth.
    'django.middleware.gzip.GZipMiddleware',

    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    # Database migration helpers:
    'south',

    # Static file management:
    'compressor',

    # Asynchronous task queue:
    'djcelery',
)

LOCAL_APPS = (
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
    'require_debug_false': {
        '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        '{{ project_name }}': {
            'handlers': ['mail_admins', 'console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## CELERY CONFIGURATION
# See: http://celery.readthedocs.org/en/latest/configuration.html#celery-task-result-expires
CELERY_TASK_RESULT_EXPIRES = timedelta(minutes=30)
# See: http://celery.github.com/celery/django/
setup_loader()
# See: http://docs.celeryq.org/en/latest/configuration.html#celery-always-eager
CELERY_ALWAYS_EAGER = DEBUG
########## END CELERY CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'
########## END WSGI CONFIGURATION


########## COMPRESSION CONFIGURATION
# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_ENABLED
COMPRESS_ENABLED = True

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
COMPRESS_CSS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS
COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]
########## END COMPRESSION CONFIGURATION


########## ALLOWED HOSTS CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [ allowed_host.strip() for allowed_host in environ.get('ALLOWED_HOSTS', '.herokuapp.com').split(',')]
########## END ALLOWED HOST CONFIGURATION

