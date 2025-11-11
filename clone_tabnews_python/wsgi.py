"""
WSGI config for clone_tabnews_python project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import traceback
import sys

from django.core.wsgi import get_wsgi_application

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception:
    traceback.print_exc()
    sys.stdout.flush()

# application = get_wsgi_application()
