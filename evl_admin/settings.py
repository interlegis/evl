"""
Django settings for evl_admin project.

Generated by 'django-admin startproject' using Django 1.10.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v=m91$ei*h!h&l23*_6yjx!l9_l+y#^!e)gtiay*tw0!5^xa9p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Email configurations

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'matheus456456@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

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
        'NAME': 'moodlews',
        # 'NAME': os.path.join(BASE_DIR, 'mydb'),
        'USER': 'escolamodelows',
        'PASSWORD': 'escolamodelo',
        'HOST': 'campeirohsabereslb.interlegis.leg.br',
        'PORT': '5432', # 8000 is default
    }
}

AUTHENTICATION_BACKENDS = (
   # 'oauth2_provider.backends.OAuth2Backend',
    # Uncomment following if you want to access the admin
    #'django.contrib.auth.backends.ModelBackend'
    'evl.login.MyOIDCAB',
)

# DEVELOPMENT

OIDC_RP_CLIENT_ID = '1f289285edb77417c69ac5d9c53ff14cc638da3a0fc31e6053763fba26cc1366' #Local
OIDC_RP_CLIENT_SECRET = '4f8397d6b8221c0ad59f009a8d9a130d99d26167487939291d093cc130524f61' #Local
OIDC_OP_AUTHORIZATION_ENDPOINT = 'http://localhost:10524/oauth/authorize' #Local
OIDC_OP_TOKEN_ENDPOINT = 'http://localhost:10524/oauth/token' #Local
OIDC_OP_USER_ENDPOINT = 'http://localhost:10524/oauth/userinfo' #Local
OIDC_RP_SIGN_ALGO = 'RS256' #Local
OIDC_OP_JWKS_ENDPOINT = 'http://localhost:10524/oauth/discovery/keys' #Local
LOGIN_REDIRECT_URL = '/baseCursos' #Local
LOGOUT_REDIRECT_URL = '/' #Local
OIDC_RP_SCOPES = 'openid profile email' #Local
OIDC_VERIFY_JWT = False #Local
OIDC_USE_NONCE = False #Local


BASE_URL = 'http://localhost:3000/'
APIKEY = '6iwXud8cubFTlGWgd8FucO6kzT8BAFXRfd7eXlZLMT3bOgPuMg'
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

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join("static"),
]
