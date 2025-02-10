"""
WSGI config for regihuer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv
load_dotenv()

from django.core.wsgi import get_wsgi_application
<<<<<<< HEAD:code/regihuer/wsgi.py

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'regihuer.settings.local')

application = get_wsgi_application()
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("SETTING"))
print("ejecua wsgi")
application = get_wsgi_application()
>>>>>>> 2c7bf022197078b280da787bf8c29fa877a6f587:regihuer/wsgi.py
