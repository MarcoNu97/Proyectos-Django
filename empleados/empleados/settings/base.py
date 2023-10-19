from pathlib import Path
##Importaciones para secret.json
import json
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

#Configuracion para el archivo secret.json
#Apertura del archivo Json en modo lectura
with open ("secret.json") as f:
    secret = json.loads(f.read())

#definicion de la funcion getSecret
def get_secret (secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg="la variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)
    
#Obtencion del valor de SECRET_KEY
SECRET_KEY = get_secret('SECRET_KEY')


# # Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Apps de terceros
    'ckeditor',
    #local apps
    'aplications.departamento',
    'aplications.empleado',
    'aplications.home',
]

#Configuracion del CK-Editor
##
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'custom',
        'height': 300,
    },

}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'empleados.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'empleados.wsgi.application'
