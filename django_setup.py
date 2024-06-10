import os
import django

os.environ.setdefault(key="DJANGO_SETTINGS_MODULE", value="first_django.settings")
django.setup()