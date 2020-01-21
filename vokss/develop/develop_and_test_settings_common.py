"""
Common development settings.
"""
import os
from django_dbdev.backends.postgres import DBSETTINGS
from vokss.default.settings import *  # noqa

THIS_DIR = os.path.dirname(__file__)

DATABASES = {
    'default': DBSETTINGS
}

# DATABASES['default']['PORT'] = 31733


DEBUG = True
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'vokss.develop.develop_urls'

INSTALLED_APPS += [
    'django_dbdev',
    # 'ievv.ievvtasks_heroku',
    'ievv_opensource.ievvtasks_development',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # During development only

IEVVTASKS_DUMPDATA_DIRECTORY = os.path.join(THIS_DIR, 'dumps')


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'verbose': {
#             'format': '[%(levelname)s %(asctime)s %(name)s %(pathname)s:%(lineno)s] %(message)s'
#         }
#     },
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'stderr': {
#             'level': 'DEBUG',
#             'formatter': 'verbose',
#             'class': 'logging.StreamHandler'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['stderr'],
#             'level': 'DEBUG',
#             'propagate': False
#         },
#         'boto': {
#             'handlers': ['stderr'],
#             'level': 'DEBUG',
#             'propagate': True
#         },
#         'django.db': {
#             'handlers': ['stderr'],
#             'level': 'INFO',  # Do not set to debug - logs all queries
#             'propagate': False
#         },
#         'sh': {
#             'handlers': ['stderr'],
#             'level': 'INFO',  # Do not set to debug - logs everything
#             'propagate': False
#
#         },
#         'urllib3': {
#             'handlers': ['stderr'],
#             'level': 'WARNING',
#             'propagate': False
#         },
#         '': {
#             'handlers': ['stderr'],
#             'level': 'DEBUG',
#             'propagate': False
#         }
#     }
# }


# redis_port = 36401
# redis_host = 'localhost'

#############
#
# Django RQ
#
#############
# RQ_QUEUES = {
#     'default': {
#         'ASYNC': False,
#         'HOST': redis_host,
#         'PORT': redis_port,
#         'DB': 0
#     }
# }