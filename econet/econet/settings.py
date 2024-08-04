"""
Django settings for econet project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from datetime import timedelta 

import os, json
import pymysql  
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent


secret_file = os.path.join(BASE_DIR, 'secrets.json')  # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1' ,'13.124.235.155']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',
	'rest_framework_simplejwt.token_blacklist',
    'users',
    'corsheaders', #CORS 관련 추가
    'boards',
    'todays',
    'rest_framework',
]

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # 인증된 요청인지 확인
        'rest_framework.permissions.IsAdminUser',  # 관리자만 접근 가능
        'rest_framework.permissions.AllowAny',  # 누구나 접근 가능
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT를 통한 인증방식 사용
    ),
}

REST_USE_JWT = True

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # CORS 관련 추가 (가장 상단에 위치)
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'econet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'econet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
    'default': { 
      	'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'econet', 
        'USER': 'admin', 
        'PASSWORD': 'econetproject', 
        'HOST': 'database-2.cdgs2mau2ch1.ap-northeast-2.rds.amazonaws.com', 
        'PORT': '3306' 
     } 
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


#CORS 관련 추가

CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:3000'
,'http://localhost:3000','http://13.124.235.155:3000']
CORS_ALLOW_ALL_ORIGINS = True #(모든 포트 허용)

CORS_ALLOW_METHODS = (
"DELETE",
"GET",
"OPTIONS",
"PATCH",
"POST",
"PUT",
)

#원하는 헤더 추가
CORS_ALLOW_HEADERS = (
"accept",
"authorization",
"content-type",
"user-agent",
"x-csrftoken",
"x-requested-with",
)
