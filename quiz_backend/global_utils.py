import os


# https://github.com/dancaron/Django-ORM/blob/master/main.py
# Django ORM Standalone Python Template
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

def init_django():
    # Avoid initializing twice
    if os.environ.get("DJANGO_SETTINGS_MODULE"):
        return
    # Turn off bytecode generation
    import sys
    # sys.dont_write_bytecode = True  # NOTE: is this needed?
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_backend.settings")
    import django
    django.setup()
