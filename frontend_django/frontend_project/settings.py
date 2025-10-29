
DEBUG = True
ALLOWED_HOSTS = ['*']  # Allow all hosts locally

INSTALLED_APPS = [
    'django.contrib.admin',          # add this
    'django.contrib.auth',           # required for admin
    'django.contrib.contenttypes',   # required for admin
    'django.contrib.sessions',       # required for admin
    'django.contrib.messages',       # optional for admin messages
    'django.contrib.staticfiles',
    'ui_app',   # your app
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',       # required
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',    # required
    'django.contrib.messages.middleware.MessageMiddleware',       # required
]
SECRET_KEY = 'g@9x!r2j#v)kq&3l8p$z+_u5b7m^h1w0'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # or add paths to your templates if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',          # required for admin sidebar
                'django.contrib.auth.context_processors.auth',         # required
                'django.contrib.messages.context_processors.messages', # required
            ],
        },
    },
]


STATIC_URL = '/static/'
STATICFILES_DIRS = []
ROOT_URLCONF = 'frontend_project.urls'
