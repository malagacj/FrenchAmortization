import os


DEBUG = os.environ.get('DEBUG', 'True')
DEBUG = False if DEBUG.lower() == 'false' else True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

if csrf_to := os.environ.get('CSRF_TRUSTED_ORIGINS'):
    CSRF_TRUSTED_ORIGINS = csrf_to.split(',')


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        'HOST': os.environ['HOST'],
        'USER': os.environ['USER'],
        'PASSWORD': os.environ['PASSWORD'],
        'NAME': os.environ['NAME'],
        'PORT': os.environ['PORT']
    }
}
