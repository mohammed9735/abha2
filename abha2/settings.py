"""
Django settings for abha2 project.
"""

from pathlib import Path
import os

# ==============================
# المسار الأساسي للمشروع
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# مفتاح الأمان (غيّره عند النشر)
# ==============================
SECRET_KEY = 'django-insecure-ضع_هنا_مفتاحك_الخاص'

# ==============================
# وضع التطوير (اجعله False في الإنتاج)
# ==============================
DEBUG = True

ALLOWED_HOSTS = []

# ==============================
# التطبيقات المثبتة
# ==============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # التطبيقات الخاصة بك
    'products',
    'orders',
    'storefront',
    'accounts',  # ✅ إضافة التطبيق الجديد
]

# ==============================
# الميدل وير
# ==============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'abha2.urls'

# ==============================
# إعدادات القوالب (Templates)
# ==============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # مسار القوالب العام
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

WSGI_APPLICATION = 'abha2.wsgi.application'

# ==============================
# قاعدة البيانات (SQLite افتراضية)
# ==============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==============================
# التحقق من كلمات المرور
# ==============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==============================
# اللغة والتوقيت
# ==============================
LANGUAGE_CODE = 'ar'            # واجهة عربية
TIME_ZONE = 'Asia/Riyadh'       # توقيت الرياض
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ==============================
# الملفات الثابتة (Static)
# ==============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ==============================
# ملفات الوسائط (Media)
# ==============================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# ==============================
# الإعدادات الافتراضية
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==============================
# إعدادات المستخدم المخصص
# ==============================
AUTH_USER_MODEL = 'accounts.CustomUser'
