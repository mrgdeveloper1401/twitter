"""
WSGI config for twitter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.conf import settings
from django.core.wsgi import get_wsgi_application

if settings.DEBUG is False:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'twitter.production.settings'
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twitter.settings')

application = get_wsgi_application()
