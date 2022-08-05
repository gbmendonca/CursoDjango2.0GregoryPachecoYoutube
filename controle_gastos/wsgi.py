##endpoint para quando coloca o sistema web no servidor 

"""
WSGI config for controle_gastos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'controle_gastos.settings')

application = get_wsgi_application()
