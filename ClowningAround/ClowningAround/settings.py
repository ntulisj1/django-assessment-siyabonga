"""Common settings and globals."""
import os
import environ
from os.path import basename


ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path("clowning_around")

env = environ.Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Site name:
SITE_NAME = basename(ROOT_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "cwyhspevbgpuhn(#iybxrc_r)l=gbks1)qxjri!rxi@b3kn)&8"

DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRD_PARTY_APPS = [
    "emoji_picker",
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "rest_framework",
]

LOCAL_APPS = ["users.apps.UsersConfig", "appointments.apps.AppointmentsConfig"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# STATIC
STATIC_ROOT = str(ROOT_DIR("staticfiles"))
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(APPS_DIR.path("static"))]


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
MEDIA_ROOT = str(APPS_DIR("media"))
MEDIA_URL = "/media/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR.path("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

# SECURITY
# SESSION_COOKIE_HTTPONLY = True
# CSRF_COOKIE_HTTPONLY = True
# SECURE_BROWSER_XSS_FILTER = True
# X_FRAME_OPTIONS = "ALLOW"

# # EMAIL
# EMAIL_BACKEND = env(
#     "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
# )
# EMAIL_TIMEOUT = 5

ROOT_URLCONF = "ClowningAround.urls"
WSGI_APPLICATION = "ClowningAround.wsgi.application"

# Database
DATABASES = {
    "OPTIONS": {"charset": "utf8mb4"},
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    },
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Django Admin URL
ADMIN_URL = "admin/"
ADMINS = [("""Ntuli Siya""", "ntulisj1@gmail.com")]
MANAGERS = ADMINS


# AUTHENTICATION
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "users:redirect"
LOGIN_URL = "account_login"


# Internationalization
LANGUAGE_CODE = "en-ZA"

TIME_ZONE = "Africa/Johannesburg"

USE_I18N = True

USE_L10N = True

USE_TZ = True

ACCOUNT_ADAPTER = "users.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "users.adapters.SocialAccountAdapter"
