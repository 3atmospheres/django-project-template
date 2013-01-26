import os
import sys
from unipath import Path

# BASIC SETUP
PROJECT_ROOT = Path(__file__).ancestor(2)
APPS_ROOT = PROJECT_ROOT.child('apps')
sys.path.insert(0, APPS_ROOT)
DEBUG = TEMPLATE_DEBUG = False
ROOT_URLCONF = '{{ project_name }}.urls'
SECRET_KEY = '{{ secret_key }}'
SITE_ID = 1
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

# MEDIA, ASSETS, ETC.
MEDIA_ROOT = PROJECT_ROOT.child('media')
MEDIA_URL = '/media/'
STATIC_ROOT = PROJECT_ROOT.child('static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [PROJECT_ROOT.child('assets')]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# TEMPLATES
TEMPLATE_DIRS = [PROJECT_ROOT.child('templates')]

# MIDDLEWARE
MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# TEMPLATE CONTEXT PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
]

# APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # third-party packages
    'compressor',
    'gunicorn',
    'south',

    # {{ project_name }} apps
]

# LOGGING
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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

## COMPRESSOR SETTINGS
COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
   ('text/less', 'lessc {infile} {outfile}'),
)
COMPRESS_CSS_FILTERS = [
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]
