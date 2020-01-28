"""
WSGI config for vokss project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vokss.settingsproxy')

#update your wsgi.py file to use dj-static:
application = Cling(get_wsgi_application())
