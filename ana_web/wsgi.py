# <<<<<<< HEAD
# ﻿"""
# =======
# """
# >>>>>>> 1463554eb3ce51ed061b9df81aeb0a691d1f2ac3
# WSGI config for ana_web project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ana_web.settings')

# application = get_wsgi_application()
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ana_web.settings')

application = get_wsgi_application()