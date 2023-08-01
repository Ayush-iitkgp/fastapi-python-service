from os import getenv

TITLE = "Alpas AI Solution"
DESCRIPTION = "Lighting fast API for Alpas AI Solution"
ENVIRONMENT = getenv('APP_ENVIRONMENT', '')
RELEASE = getenv('GIT_HASH_SHORT', 'NONE')

PORT = int(getenv('APP_PORT', '3000'))
HOST = getenv('APP_HOST')
DEBUG = getenv('APP_DEBUG') == '1'

TIMEZONE = getenv('APP_TIMEZONE', 'UTC')  # Default is 'UTC'
DATABASE_URL = getenv('DATABASE_URL')
DATABASE_NAME = getenv('DATABASE_NAME')
DATABASE_TLS_ENABLED = getenv('DATABASE_TLS_ENABLED') == '1'
DATABASE_TLS_CA_FILE = getenv('DATABASE_TLS_CA_FILE')