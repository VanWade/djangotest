"""
Django settings for celerytest project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from __future__ import absolute_import
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l+f@ryv6bo9w65*vo3(x()4!8y6gjvcten7c3&cb#c5(n(7n3&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'crontest',
    'feedback',
    'photos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'celerytest.urls'

TEMPLATES = [
    {
        'BACKEND':'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'celerytest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# 关于celery的配置
import djcelery
from celery.schedules import crontab
djcelery.setup_loader()
BROKER_URL = 'redis://127.0.0.1:6381'
# BROKER_URL = 'redis://:密码@主机地址:端口号/数据库号'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6381'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
from datetime import timedelta

# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# CELERYBEAT_SCHEDULE = {
#     'task1': {
#         'task': 'crontest.tasks.test_celery',
#         'schedule': crontab(minute=u'58', hour=u'10',),
#         # 'schedule': timedelta(seconds=3),
#         'args': (16, 16)
#     },
#     'task2': {
#         'task': 'crontest.tasks.test_celery',
#         'schedule': crontab(minute=u'59', hour=u'10', ),
#         # 'schedule': timedelta(seconds=3),
#         'args': (16, 20)
#     },
# }
CELERYD_LOG_FILE = BASE_DIR + "/logs/celery/celery.log" # log路径
CELERYBEAT_LOG_FILE = BASE_DIR + "/logs/celery/beat.log" # beat log路径

# Emails
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER =
EMAIL_HOST_PASSWORD =
DEFAULT_FROM_EMAIL =