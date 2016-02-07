import os
import dj_database_url
from config.base_settings import *

INSTALLED_APPS += [
    'bob',
]

DATABASES['bob_db'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'bob_db',
    'USER': os.environ.get('DB_USER'),
    'PASSWORD': os.environ.get('DB_PASS'),
}

DATABASE_ROUTERS += ['config.bob.db_router.BobDBRouter']

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['bob_db'].update(db_from_env)
