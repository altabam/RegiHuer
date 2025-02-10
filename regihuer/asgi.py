"""
ASGI config for regihuer project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from dotenv import load_dotenv
load_dotenv()

from django.core.asgi import get_asgi_application

<<<<<<< HEAD:code/regihuer/asgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'regihuer.settings.local')

=======
"""os.environ.setdefault("DJANGO_SETTINGS_MODULE", "regihuer.settings.local")"""
os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("SETTING"))
print(os.getenv('DJANGO_SETTINGS_MODULE'))
>>>>>>> 2c7bf022197078b280da787bf8c29fa877a6f587:regihuer/asgi.py
application = get_asgi_application()
