"""
WSGI config for velazquez project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "velazquez.settings")

from dj_static import Cling, MediaCling
from whitenoise.django import DjangoWhiteNoise
#if settings.DEBUG is False:
#	application = get_wsgi_application()	
#else:
#	print 'media'
application = Cling(MediaCling(get_wsgi_application()))




