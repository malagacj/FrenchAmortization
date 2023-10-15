import os


DEBUG = os.environ.get('DEBUG', 'True')
if DEBUG.lower() == 'false':
    DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

if csrf_to := os.environ.get('CSRF_TRUSTED_ORIGINS'):
    CSRF_TRUSTED_ORIGINS = csrf_to.split(',')
