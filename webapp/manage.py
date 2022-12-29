#!/c/Users/hyder/AppData/Local/Microsoft/WindowsApps/python
import os
import sys
import django
import sphinx
import subprocess
import flake8
from django.core.exceptions import ImproperlyConfigured
from django.core.management import call_command, execute_from_command_line
from flake8.main.cli import main as flake8_main

# Check Django version
if django.VERSION[:2] < (1, 9):
    raise Exception('This project requires Django 1.9 or later')

# Get secret key
def get_secret_key(setting):
    try:
        from myproject.settings import secret_key
    except ImportError:
        raise ImproperlyConfigured("Set the %s environment variable" % setting)
    return secret_key

SECRET_KEY = get_secret_key('SECRET_KEY')

# Set Django settings module
def main(settings_module):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    execute_from_command_line(sys.argv)

# Run development server
def run_server():
    call_command('runserver')

# Create superuser
def create_superuser():
    call_command('createsuperuser')

# Run tests
def run_tests():
    call_command('test')

# Load fixtures
def load_fixtures():
    call_command('loaddata', 'fixture1', 'fixture2')

# Execute management command
def run_management_command(command_name, *args):
    call_command(command_name, *args)

# Run Django shell
def run_shell():
    call_command('shell')

# Generate documentation
def generate_docs():
    subprocess.check_call(['sphinx-build', '-b', 'html', 'docs', 'docs/_build/html'])

# Check code style
def check_code_style():
    sys.exit(flake8_main())

# Generate requirements file
def generate_requirements_file():
    subprocess.check_call(['pip', 'freeze', '>', 'requirements.txt'])

if __name__ == '__main__':
    main('myproject.settings.production')
