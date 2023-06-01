import os

# SECURITY WARNING: keep the secret key used in production secret!

# Note from Gen: You can find this in the OysterCloud Configuration page under App settings > SECRET_KEY
SECRET_KEY = os.getenv('410d39c144c1bb7a1fe05a01960f6f80fe4b86f079c4e99cd70db81d14193eb5')

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
conn_str = os.environ['dbname=oystercloud2-database host=oystercloud2-server.postgres.database.azure.com port=5432 sslmode=require user=mrttvqovox password=Y270OQ2LR85MAP84$']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=conn_str_params['mrttvqovox'],
    dbpass=conn_str_params['Y270OQ2LR85MAP84$'],
    dbhost=conn_str_params['oystercloud2-server.postgres.database.azure.com'],
    dbname=conn_str_params['oystercloud2-server']
)