from codecademy_todo.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd#i)%bn4#ym7)+xlcu=_@$gx(@6qw8d+o4x_yh)bf9d8kevo5u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
