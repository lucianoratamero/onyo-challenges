import os
import dj_database_url
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

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['ana_db'].update(db_from_env)
