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
EMAIL_HOST_USER = 'diego.rada8@gmail.com'
EMAIL_HOST_PASSWORD = '4547533'
EMAIL_PORT = 587