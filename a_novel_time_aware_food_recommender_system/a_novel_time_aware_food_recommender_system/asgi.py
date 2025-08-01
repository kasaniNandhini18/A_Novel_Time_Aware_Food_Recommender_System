"""
ASGI config for a_novel_time_aware_food_recommender_system.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_novel_time_aware_food_recommender_system.settings')

application = get_asgi_application()
