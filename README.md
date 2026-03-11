# Django Starter Project Template

A comprehensive Django project template with pre-configured authentication, extended permission framework, and development tooling to jumpstart new Django applications.


## Quick Setup
1. Cloning and Re-initialization of project after making necessary changes.
    ```bash
    $ gh repo clone developermayank/django-starter-template PROJECT_FOLDER
    $ cd PROJECT_FOLDER
    $ rm -rfd .git
    $ git init .
    $ git commit -am 'Project Initialized'
    
    ----------OR---------

    $ gh repo create --template developermayank/django-starter-template --private --clone LOCAL_DIRECTORY

    ----------
    $ uv sync
    ```
2. Make necessary changes to pyproject.toml regarding project description, version, authors etc.
3. Update the database configuration in `config/settings.py` if you want to use a database other than SQLite.
4. Rename .env.sample to .env and update the environment variables as needed.
5. Run the development server to verify everything is set up correctly.
    ```bash
    $ uv run manage.py runserver
    ```


## Features
- Custom Auth User Model
- Extended Permission Framework to support dynamic permissions, without hardcoding into model Meta
- Default VS Code settings with extensions recommendations


## Load Testing
```bash
winget install hatoo.oha
```