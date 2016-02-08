import dj_database_url

from config.base_settings import *

INSTALLED_APPS += ['api.v0.ana','api.v0.bob']

CURRENT_BOB_API_URL = os.environ.get('CURRENT_BOB_API_URL')

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
