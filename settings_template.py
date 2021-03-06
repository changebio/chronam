import os

DIRNAME = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

ADMINS = (
)

MANAGERS = ADMINS

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = ''
MEDIA_URL = ''

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

STATIC_URL = '/media/'
STATIC_ROOT = os.path.join(DIRNAME, '.static-media')

ROOT_URLCONF = 'chronam.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chronam',
        'USER': 'chronam',
        'PASSWORD': 'pick_one',
        }
    }

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'px2@!q2(m5alb$0=)h@u*80mmf9cd-nn**^y4j2j&+_8h^n_0f'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'chronam.core.middleware.TooBusyMiddleware',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(DIRNAME, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'chronam.core.context_processors.extra_request_info',
                'chronam.core.context_processors.newspaper_info',
            ],
            'debug' : DEBUG,
        },
    },
]


INSTALLED_APPS = (
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'djcelery',
    'kombu.transport.django',
    'chronam.core',
)

BROKER_URL = 'django://'

THUMBNAIL_WIDTH = 360

DEFAULT_TTL_SECONDS = 86400  # 1 day
PAGE_IMAGE_TTL_SECONDS = 60 * 60 * 24 * 7 * 2  # 2 weeks
API_TTL_SECONDS = 60 * 60  # 1 hour
FEED_TTL_SECONDS = 60 * 60 * 24 * 7

USE_TIFF = False


ESSAYS_FEED = "http://essays.loc.gov/feed/"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
        'TIMEOUT': 4838400,  # 2 months
    }
}

IS_PRODUCTION = False
CTS_USERNAME = 'username'
CTS_PASSWORD = 'password'
CTS_PROJECT_ID = 'ndnp'
CTS_QUEUE = 'ndnpingestqueue'
CTS_SERVICE_TYPE = 'ingest.NdnpIngest.ingest'
CTS_URL = "https://cts.loc.gov/transfer/"

MAX_BATCHES = 0

import multiprocessing
#TOO_BUSY_LOAD_AVERAGE = 1.5 * multiprocessing.cpu_count()
TOO_BUSY_LOAD_AVERAGE = 64 

SOLR = "http://localhost:8983/solr"
SOLR_LANGUAGES = ("eng", "fre", "spa", "ger", "ita",)

STORAGE = '/opt/chronam/data/'
BATCH_STORAGE = os.path.join(STORAGE, "batches")
BIB_STORAGE = os.path.join(STORAGE, "bib")
OCR_DUMP_STORAGE = os.path.join(STORAGE, "ocr")
COORD_STORAGE = os.path.join(STORAGE, "word_coordinates")


BASE_CRUMBS = [{'label':'Home', 'href': '/'}]

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']
import djcelery
djcelery.setup_loader()
