import os
from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'x7cuyre=cc^@l$6$0ky3-&aia-n*ya)*h#ubl=zko6@$57@_jp'

DEBUG = True

ALLOWED_HOSTS = []

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    )

LOCAL_APPS = (
    'apps.usuarios',
    'apps.venezuela', 
    'apps.administradora',
    'apps.pagos',
    )

THIRD_PARTY_APPS = (
    #'south',
    #'django_extensions'
    )

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'condominios.urls'

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates/administradora'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'condominios.wsgi.application'

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

AUTH_USER_MODEL = 'usuarios.Usuario'

LOGIN_REDIRECT_URL = "condominio/"

LOGIN_URL = '/'