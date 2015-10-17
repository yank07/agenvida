"""
Django settings for agenvida project.
Generated by 'django-admin startproject' using Django 1.8.4.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+%2!f3=ryc=w7$by32hff#d)ctb6)=$xle&l=e$r)(q^ej+$do'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainApp',
    'rest_framework',#REST FRAMEWORK
    'oauth2_provider', #TOKEN
    'social.apps.django_app.default', #TOKEN SOCIAL
    'rest_framework_social_oauth2', #TOKEN SOCIAL
    'corsheaders', #Permite post de otros dominios
   

)

MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
     # CORS
    'corsheaders.middleware.CorsMiddleware',
    # ...


    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

)

# Esto sirve para que pueda hacer consultas desde otro dominio
CORS_ORIGIN_REGEX_WHITELIST = ('^http://localhost:8100$', )
CORS_ALLOW_CREDENTIALS = True
OAUTH_EXPIRE_DELTA = 360000000 # 100.000 horas;


ROOT_URLCONF = 'agenvida.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                BASE_DIR + '/templates/',
                
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'agenvida.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
import dj_database_url
DATABASES = { 'default': dj_database_url.config() }
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

AUTHENTICATION_BACKENDS = (
  

     # Facebook OAuth2
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',

    # django-rest-framework-social-oauth2
    'rest_framework_social_oauth2.backends.DjangoOAuth2',

    # Django
    'django.contrib.auth.backends.ModelBackend',
  

)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',        
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),
}



ANONYMOUS_USER_ID = 1

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}
}

SOCIAL_AUTH_FACEBOOK_KEY = '524418254291199'
SOCIAL_AUTH_FACEBOOK_SECRET = '80587a95990df049b8208dd6e6e83faa'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'es_PY',
  'fields': 'id, name, email, age_range'
}


LOGIN_REDIRECT_URL = '/'

DJOSER = {
    'DOMAIN': 'agenvida.herokuapp.com',
    'SITE_NAME': 'Agenvida',
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'agenvida@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = 587
EMAIL_USE_TLS = True


