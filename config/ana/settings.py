import os

from config.base_settings import *

INSTALLED_APPS += [
    'ana',
]

DATABASES['ana_db'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'ana_db',
    'USER': os.environ.get('DB_USER'),
    'PASSWORD': os.environ.get('DB_PASS'),
}

DATABASE_ROUTERS += ['config.ana.db_router.AnaDBRouter']


'''
Configuration needed to fully decouple APIs
'''

CURRENT_BOB_API_URL = 'http://lucianoratamero-onyo-bob.heroku.com/api/v0/bob/'
