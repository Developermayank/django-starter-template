# Django Starter Project Template
Django starter template is created for easy to use.

## Initialization
'''
    uv sync
    uv python install 3.14

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
'''

## Features
- Custom Auth Model
- Extended Permission Framework to support dynamic permissions, without hardcoding into model Meta
- Default VS Code settings with extensions recommendations

## Packages

- python-decouple>=3.8
- mysqlclient>=2.2.8 [DEV]
- psycopg>=3.3.3 [DEV]
- django-ninja>=1.5.3 [DEV]