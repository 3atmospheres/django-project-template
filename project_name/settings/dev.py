from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'autocommit': True,
        }
    }
}

DEBUG = TEMPLATE_DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
COMPRESS_ENABLED = False

try:
    import debug_toolbar
except ImportError:
    pass
else:
    INSTALLED_APPS.append('debug_toolbar')
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE_CLASSES.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'cache_panel.CachePanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
        'debug_toolbar.panels.profiling.ProfilingDebugPanel',
    )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
