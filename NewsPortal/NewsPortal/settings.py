"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path
import logging

logger = logging.getLogger('django')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pxtv2auh+^s=p3eei2@zil64zr#jrczkqc=@(0ic#eo%2c@f70'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    'accounts',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler'
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware',

]

ROOT_URLCONF = 'NewsPortal.urls'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPortal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский')
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = "/news"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # вывод сообщения в консоль
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'titan182@yandex.ru'
EMAIL_HOST_PASSWORD = 'oxdegiryrdijzlaa'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = 'titan182@yandex.ru'

SERVER_EMAIL = 'titan182@yandex.ru'

APSHEDULER_DARETIME_FORMAT = 'N, j, Y, f:s a'
APSHEDULER_RUN_NOW_TIMEOUT = 25
SITE_URL = 'http://127.0.0.1:8000'

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),  # Указываем, куда будем сохранять кэшируемые файлы!
    }
}


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'style': '{',
#     'formatters': {
#         'simple': {
#             'format': '%(acstime)s %(levelname)s %(message)s',
#             'datefmt': "%D.%M.%Y %H-%M-%S"
#         },
#         'format_warning': {
#             'format': '%(acstime)s %(levelname)s %(message)s %(pathname)s',
#             'datefmt': "%D.%M.%Y %H-%M-%S"
#         },
#         'format_error': {
#             'format': '%(acstime)s %(levelname)s %(message)s %(exc_info)s',
#             'datefmt': "%D.%M.%Y %H-%M-%S"
#         },
#         'format_general': {
#             'format': '%(acstime)s %(levelname)s %(module)s %(message)s',
#             'datefmt': "%D.%M.%Y %H-%M-%S"
#         },
#         'errors': {
#             'format': '%(acstime)s %(levelname)s %(pathname)s %(message)s (exc_info)s',
#             'datefmt': "%D.%M.%Y %H-%M-%S"
#         },
#         'format_email': {
#             'format': '%(acstime)s %(levelname)s %(message)s %(pathname)s',
#             'datefmt': "%D.%M.%Y %H-%M-%S"
#         },
#         'format_security': {
#             'format': '%(acstime)s %(levelname)s %(module)s %(message)s',
#             'datefmt': "%D.%M.%Y %H-%M-%S"
#         },
#     },
#
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#     },
#
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'console_warning': {
#             'level': 'WARNING',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'format_warning'
#         },
#         'console_error': {
#             'level': 'ERROR',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'format_error'
#         },
#         'general': {
#             'level': 'INFO',
#             'filters': ['require_debug_false'],
#             'class': 'logging.FileHandler',
#             'filename': 'logs/general.log',
#             'formatter': 'format_general',
#         },
#         'errors': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': 'logs/errors.log',
#             'formatter': 'errors'
#         },
#         'security': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': 'logs/security.log',
#             'formatter': 'format_security'
#         },
#         'mail_admin': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'formatter': 'format_email'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'console_warning', 'console_error', 'general'],
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['errors', 'mail_admin'],
#             'propagate': True,
#         },
#         'django.server': {
#             'propagate': True,
#         },
#         'django.template': {
#             'handlers': ['errors'],
#             'propagate': True,
#         },
#         'django.db.backends': {
#             'handlers': ['errors'],
#             'propagate': True,
#         },
#         'django.security': {
#             'handlers': ['security'],
#             'propagate': True,
#         },
#
#     },
#
# }