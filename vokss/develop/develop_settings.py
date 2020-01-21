# from buyclip.buyclip_rq import devrun_rq_runnable
from ievv_opensource.utils import ievvdevrun
from ievv_opensource.utils import ievvbuildstatic

from .develop_and_test_settings_common import *

INSTALLED_APPS += [
    'ievv_opensource.ievv_developemail',
]

IEVVTASKS_DEVRUN_RUNNABLES = {
    'default': ievvdevrun.config.RunnableThreadList(
        ievvdevrun.runnables.dbdev_runserver.RunnableThread(),
        # ievvdevrun.runnables.redis_server.RunnableThread(port='36401'),
        ievvdevrun.runnables.django_runserver.RunnableThread(port=8007),
    ),
    'design': ievvdevrun.config.RunnableThreadList(
        ievvdevrun.runnables.dbdev_runserver.RunnableThread(),
        # ievvdevrun.runnables.redis_server.RunnableThread(port='36401'),
        ievvdevrun.runnables.django_runserver.RunnableThread(port=8007),
        ievvdevrun.runnables.ievv_buildstatic.RunnableThread()
    ),
}

IEVVTASKS_HEROKUDEPLOY = {
    'production': {
        'release_type': 'production',
        'heroku_appname': 'buyclip-prod',
        'require_git_branch': 'production',
        'pre_gitpush_heroku_commands': [
        ],
        'post_gitpush_heroku_commands': [
            ['maintenance:on'],
            ['run', 'python manage.py migrate'],
            ['maintenance:off'],
        ],
    },
}

# IEVVTASKS_RECREATE_DEVDB_POST_MANAGEMENT_COMMANDS = [
#     {
#         'name': 'ievvtasks_customsql',
#         'args': ['-i', '-r'],
#     },
# ]

# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]

# INSTALLED_APPS += [
#     'debug_toolbar',
# ]

# Required for django debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

EMAIL_BACKEND = 'ievv_opensource.ievv_developemail.email_backend.DevelopEmailBackend'

