import os


DEBUG = os.environ.get('DEBUG', 'True')
if DEBUG.lower() == 'false':
    DEBUG = False

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')
