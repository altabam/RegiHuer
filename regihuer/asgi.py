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

"""os.environ.setdefault("DJANGO_SETTINGS_MODULE", "regihuer.settings.local")"""
os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("SETTING"))
print(os.getenv('DJANGO_SETTINGS_MODULE'))
application = get_asgi_application()
