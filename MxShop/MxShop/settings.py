"""
Django settings for MxShop project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
sys.path.insert(0, os.path.join(BASE_DIR, "extra_apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q$6plruxhzwtizkwv=*uen$=0*enrohiwe+o)^9r1*4ee54@m='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'xadmin',
    'crispy_forms',
    'reversion',
    'goods',
    'trade',
    'user_operation',
    'DjangoUeditor',
    'rest_framework',
    'django_filters',  # 过滤
    'corsheaders',  # 跨域
    'rest_framework.authtoken',  # 用户验证
    'social_django',  # 微博登陆
]

AUTH_USER_MODEL = 'users.UserProFile'  # 替换系统的models——user

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 跨域
    # 'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True  # 跨域

ROOT_URLCONF = 'MxShop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 第三方登陆
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'MxShop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'mxshop',
        'USER': 'root',
        'PASSWORD': 'admin123456',
        'HOST': 'localhost',
        'PORT': '3306',
        # 'OPTIONS': {'init_command': 'SET storage_engine=INNODB;'} #设置mysql的索引，这种有时候会出错
        "OPTIONS": {"init_command": "SET default_storage_engine=INNODB;"}  # 需要使用这种来设置Mysql数据库的索引
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

# LANGUAGE_CODE = 'en-us'

LANGUAGE_CODE = 'zh-hans'  # 语言改为中文

# TIME_ZONE = 'UTC'

TIME_ZONE = 'Asia/Shanghai'  # 时间改为中国上海

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False  # 改为False,让django使用本地时间

# 格式化后台内容的显示时间
USE_L10N = False
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'

WSGI_APPLICATION = 'MxShop.wsgi.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
    # 第三方登陆
    'social_core.backends.weibo.WeiboOAuth2',
    'social_core.backends.weixin.WeixinOAuth2',
    'social_core.backends.qq.QQOAuth2',
    # ...
    'django.contrib.auth.backends.ModelBackend',
)

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [(os.path.join(BASE_DIR, "static")), ]  # 配置静态文件的目录

REST_FRAMEWORK = {
    '''
    REST_FRAMEWORK的配置
    '''
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',  # 验证用户登录信息，输入用户名密码
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # Token认证
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        # drf的限速，防止爬虫请求过快，限速的类
        'rest_framework.throttling.AnonRateThrottle',  # 未登录用户
        'rest_framework.throttling.UserRateThrottle'  # 登陆用户
    ),
    'DEFAULT_THROTTLE_RATES': {
        # drf的限速，防止爬虫请求过快，限制时间
        'anon': '100/day',  # 匿名用户限速时间
        'user': '1000/day'  # 登陆用户限制时间
    }
}

JWT_AUTH = {
    '''
    JWT的配置
    '''
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=3),  # 设置jwt的验证过期时间3天
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

REGEX_MOBILE = "^((\d3)|(\d{3}\-))?13[0-9]\d{8}|15[89]\d{8}"  # 手机号正则验证

# 云片网API设置
API_KEY = "d198jdijdidnjaa88880cb5bbfe69659d"

# STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# 支付宝秘钥的配置
PUBLIC_KEY = os.path.join(BASE_DIR, "apps/trade/keys/AliPay_Key.txt")
PRIVATE_KEY = os.path.join(BASE_DIR, "apps/trade/keys/private_2048.txt")
ALIPAY_URL = "http://903.999.114.138:8000/alipay/return/"
ALIPAY_APPID = "20160989150058998828737374419562"

# 设置res_api缓存的过期时间
REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 5 * 5
}

#第三方微博登陆的配置
SOCIAL_AUTH_WEIBO_KEY = 'foobar'
SOCIAL_AUTH_WEIBO_SECRET = 'bazqux'

#第三方QQ登陆的配置
SOCIAL_AUTH_QQ_KEY = 'foobar'
SOCIAL_AUTH_QQ_SECRET = 'bazqux'

#第三方微信登陆的配置
SOCIAL_AUTH_WEIXIN_KEY = 'foobar'
SOCIAL_AUTH_WEIXIN_SECRET = 'bazqux'

#配置第三方登陆，如果登陆成功指定跳转的url
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/index/'