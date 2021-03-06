"""
Django settings for evl_admin project.

Generated by 'django-admin startproject' using Django 1.10.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from unipath import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v=m91$ei*h!h&l23*_6yjx!l9_l+y#^!e)gtiay*tw0!5^xa9p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'mozilla_django_oidc',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'localflavor',
    'oauth2_provider',
    'corsheaders',
    'evl',
    'cursos',
    'fale_conosco',
    'certificado',
    'comprovante',
    'administrador',
    'adesao_institucional',
]
# CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    #'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mozilla_django_oidc.middleware.SessionRefresh',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'evl_admin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('EVL_DB_NAME'),
        'USER': os.environ.get('EVL_DB_USER'),
        'PASSWORD': os.environ.get('EVL_DB_PASS'),
        'HOST': os.environ.get('EVL_DB_HOST'),
        'PORT': os.environ.get('EVL_DB_PORT'), # 8000 is default
    }
}

AUTHENTICATION_BACKENDS = (
   # 'oauth2_provider.backends.OAuth2Backend',
    # Uncomment following if you want to access the admin
    #'django.contrib.auth.backends.ModelBackend'
    'evl.login.MyOIDCAB',
)

URL_CENTRAL = os.environ.get('EVL_CENTRAL_URL_BASE')
OIDC_RP_CLIENT_ID = str(os.environ.get('EVL_TOKEN_APPLICATION_ID'))
OIDC_RP_CLIENT_SECRET = str(os.environ.get('EVL_TOKEN_SECRET'))
OIDC_OP_AUTHORIZATION_ENDPOINT = str(os.environ.get('EVL_CENTRAL_URL_BASE')) + '/oauth/authorize'
OIDC_OP_TOKEN_ENDPOINT = str(os.environ.get('EVL_CENTRAL_URL_BASE')) + '/oauth/token'
OIDC_OP_USER_ENDPOINT = str(os.environ.get('EVL_CENTRAL_URL_BASE')) + '/oauth/userinfo'
OIDC_RP_SIGN_ALGO = 'RS256'
OIDC_OP_JWKS_ENDPOINT = str(os.environ.get('EVL_CENTRAL_URL_BASE')) + '/oauth/discovery/keys'
LOGIN_REDIRECT_URL = '/aluno'
LOGOUT_REDIRECT_URL = '/'
OIDC_RP_SCOPES = 'openid profile email'
OIDC_VERIFY_JWT = False
OIDC_USE_NONCE = False

APIKEY = os.environ.get('EVL_WS_APIKEY')
BASE_URL = os.environ.get('EVL_WS_URL_BASE')

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'},
    'ACCESS_TOKEN_EXPIRE_SECONDS': 36000,
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

BASE_DIR = Path(__file__).ancestor(1)
PROJECT_DIR = Path(__file__).ancestor(2)

STATIC_URL = '/static/'
STATIC_ROOT = PROJECT_DIR.child('collected_static')

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
    ("administrador", PROJECT_DIR.child('administrador') + "/static"),
    ("cursos", PROJECT_DIR.child('cursos') + '/static'),
    ("certificado", PROJECT_DIR.child('certificado') + '/static'),
    ("fale_conosco", PROJECT_DIR.child('fale_conosco') + '/static'),
    ("evl", PROJECT_DIR.child('evl') + '/static'),
    ("comprovante", PROJECT_DIR.child('comprovante') + '/static'),
    ("adesao_institucional", PROJECT_DIR.child('adesao_institucional') + '/static'),
)
