from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'admincondominios',
        'USER': 'postgres',
        'PASSWORD': '18189312',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, '../static/administradora'),
	)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'correo@gmail.com'
EMAIL_HOST_PASSWORD = 'clave'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'correo@gmail.com'