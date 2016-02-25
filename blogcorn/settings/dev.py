from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r4v9lobye@o9q4lt$2&8)e5xz!e3b6-8p5g1tjz+w(9q)q7!-o'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
