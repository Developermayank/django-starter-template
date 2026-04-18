@echo off

:: Show help if no arguments are provided or if 'help' is typed
if "%1"=="" goto HELP
if "%1"=="help" goto HELP

:: 1. Specific shortcuts
if "%1"=="run"              goto RUNSERVER
if "%1"=="mm"               goto MAKEMIGRATIONS
if "%1"=="m"                goto MIGRATE
if "%1"=="migrate"          goto MIGRATE

:: Show all Django commands: 'show' or 'list' or 'ls
if "%1"=="show"     goto SHOW_COMMANDS
if "%1"=="list"     goto SHOW_COMMANDS


:: 2. Default: Pass everything else to manage.py
uv run python manage.py %*
goto END

:: --- Labels ---

:HELP
echo.
echo Django Helper (dj.bat)
echo -------------------------------------------------------------
echo dj run                     - Run development server
echo dj mm [app]                - Make new migrations
echo dj m/migrate [app]         - Run migrations
echo dj show/list               - Show all manage.py command
echo dj [command]               - Run any manage.py command (e.g., dj shell)
echo.
goto END

:RUNSERVER
uv run python manage.py runserver %*
goto END

:MAKEMIGRATIONS
uv run python manage.py makemigrations %*
goto END

:MIGRATE
uv run python manage.py migrate %*
goto END

:SHOW_COMMANDS
uv run python manage.py help
goto END

:END
