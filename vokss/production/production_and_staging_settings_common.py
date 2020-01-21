import os
from urllib.parse import urlparse
from vokss.default.settings import *  # noqa

ROOT_URLCONF = 'buyclip.project.production.production_urls'

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

########################################
# Cache
########################################
redis_url = urlparse(os.environ.get('REDIS_URL'))

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': f'{redis_url.hostname}:{redis_url.port}',
        'OPTIONS': {
            'PASSWORD': redis_url.password,
            'DB': 0,
        }
    }
}

#: Name of the django-rq queue used for async email-sending. This queue must be configured in settings.RQ_QUEUES.
IEVV_RQ_EMAIL_BACKEND_QUEUENAME = 'default'

RQ_QUEUES = {
    'default': {
        'ASYNC': True,
        'HOST': redis_url.hostname,
        'PASSWORD': redis_url.password,
        'PORT': redis_url.port,
        'DB': 0,
        'DEFAULT_TIMEOUT': 60 * 60 * 2  # 2 hours
    },
    'long_running_tasks': {
        'ASYNC': True,
        'HOST': redis_url.hostname,
        'PASSWORD': redis_url.password,
        'PORT': redis_url.port,
        'DB': 0,
        'DEFAULT_TIMEOUT': 60 * 60 * 20  # 20 hours
    }
}

########################################
# Cache
########################################
# redis_url = urlparse(os.environ.get('REDISCLOUD_URL'))
# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.RedisCache',
#         'LOCATION': '{hostname}:{port}'.format(
#             hostname=redis_url.hostname, port=redis_url.port),
#         'OPTIONS': {
#             'PASSWORD': redis_url.password,
#             'DB': 0,
#         }
#     }
# }

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
STATIC_ROOT = 'buyclip/staticfiles'
STATIC_URL = '/static/'

#################################
# AWS settings
#################################
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_FILE_OVERWRITE = False
# AWS_S3_SECURE_URLS = False
# AWS_ACCESS_KEY_ID = os.environ['DJANGO_AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = os.environ['DJANGO_AWS_SECRET_ACCESS_KEY']
# AWS_STORAGE_BUCKET_NAME = os.environ['DJANGO_AWS_STORAGE_BUCKET_NAME']
# MEDIA_URL = '//{bucket}.s3.amazonaws.com/'.format(bucket=AWS_STORAGE_BUCKET_NAME)

# Where to put user uploaded files relative to the root of the bucket?
MEDIA_ROOT = 'django_media_root'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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
