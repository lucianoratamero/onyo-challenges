from config.base_settings import *

INSTALLED_APPS += [
    'ana',
    'bob',
]

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
