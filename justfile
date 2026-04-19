# use bash (important for consistency)
set shell := ["bash", "-cu"]

# auto-activate venv (Windows + Git Bash)
manage := "uv run manage.py"

# default task
default:
    @just --list

# run dev server
run:
    {{manage}} runserver

# migrations
makemig:
    {{manage}} makemigrations

mig:
    {{manage}} migrate

# django shell
shell:
    {{manage}} shell

# tests
test:
    {{manage}} test

# superuser
createsuper:
    {{manage}} createsuperuser