from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd809agelvpvn4e',
        'USER': 'uqsufslbkoanst',
        'PASSWORD':'V-oRMAxzGMYvWUHJXjLw-vSp7b',
        'HOST': 'ec2-75-101-143-150.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
STATIC_ROOT ='staticfiles'

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