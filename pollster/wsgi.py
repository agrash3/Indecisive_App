<<<<<<< HEAD
"""
WSGI config for pollster project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
=======
<<<<<<< HEAD
=======
"""
WSGI config for pollster project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
>>>>>>> dd8e683bf902422332c15d70d55d3d53b3553e2d
>>>>>>> c915ff6c59d82525151f3696c383766d57fd83e2

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pollster.settings')

application = get_wsgi_application()