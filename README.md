# Django Starter Project Template
Django Project Template

## Usage
-   _gh repo create --template developermayank/django-starter-template --private --clone_ **LOCAL_DIRECTORY**
- _gh repo clone developermayank/django-starter-template && rm -rfd .git && git init . && git commit -am 'Project Template Initialized'_

## Sample Commands
```
    uv sync
    uv sync --group api drf linux mysql postgres ml cli
    uv python install 3.14

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
```

## Features
- Custom Auth User Model
- Extended Permission Framework to support dynamic permissions, without hardcoding into model Meta
- Default VS Code settings with extensions recommendations

## Packages