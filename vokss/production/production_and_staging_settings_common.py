import os
from urllib.parse import urlparse
from vokss.default.settings import *  # noqa

ROOT_URLCONF = 'vokss.production.production_urls'

DEBUG = False
LANGUAGE_CODE = 'uk'
INSTALLED_APPS += [
    'gunicorn',
]

###########################
# Database
###########################
DATABASES = {}

# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES['default'] = dj_database_url.config()

###########################
# Templates
###########################
TEMPLATES[0]['OPTIONS']['debug'] = False

#################################
# Heroku settings
#################################
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# BASE_DIR = os.path.dirname(
#     os.path.dirname(
#         os.path.dirname(
#             os.path.dirname(
#                 os.path.dirname(os.path.abspath(__file__))))))
STATIC_ROOT = 'atelier/staticfiles'
STATIC_URL = '/static/'


# Where to put user uploaded files relative to the root of the bucket?
MEDIA_ROOT = 'django_media_root'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

############################
# Logging
############################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s %(asctime)s %(name)s %(pathname)s:%(lineno)s] %(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'stderr': {
            'level': 'DEBUG',
            'formatter': 'verbose',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['stderr'],
            'level': 'INFO',
            'propagate': False
        },
        'boto': {
            'handlers': ['stderr'],
            'level': 'WARNING',
            'propagate': True
        },
        'django.db': {
            'handlers': ['stderr'],
            'level': 'INFO',  # Do not set to debug - logs all queries
            'propagate': False
        },
        '': {
            'handlers': ['stderr'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

# The SECRET_KEY MUST be set as an environment variable in prod
# You can generate this using ``ievv generate_django_secret_key``
# from ievv_opensource 4.2+ (requires ievv_opensource.ievvtasks_common in
# INSTALLED_APPS).
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# for emailing site error to my email address this account email is used
ADMINS = [
    ('vitamal', 'vitamal@ukr.net'),
]

# settings for SendGrid email box using
SENDGRID_API_KEY = os.getenv('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')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
