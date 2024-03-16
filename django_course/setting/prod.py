from django_course.settings import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z9l!_k*xde21djo@4u54w63hj1+q#v06+(#tyhm!&w26p!7h5_'

CSRF_COOKIE_SECURE=True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mahsamohajeri.ir','www.mahsamohajeri.ir','127.0.0.1']

SITE_ID=4

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT= BASE_DIR / 'static'
MEDIA_ROOT= BASE_DIR / 'media'


STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

# CSRF_COOKIE_SECURE=True

X_FRAME_OPTIONS = "SAMEORIGIN"






#__________________________________________________________
# این هارو توی سایتم نوشتم
# SECURE_BROWSER_XSS_FILTER = True
# CSRF_COOKIE_SECURE=True
# X_FRAME_OPTIONS = 'SAMEORIGINE'

# SECURE_CONTENT_TYPE_NOSNIFF = True
# ## Strict-Transport-Security
# SECURE_HSTS_SECONDS = 15768000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# ## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
# SECURE_SSL_REDIRECT = True 

# # for more security
# CSRF_COOKIE_SECURE = True
# CSRF_USE_SESSIONS = True
# CSRF_COOKIE_HTTPONLY = True
# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_SAMESITE = 'Strict'