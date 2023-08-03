from os import getenv

TITLE = "Alpas AI Solution"
DESCRIPTION = "Lighting fast API for Alpas AI Solution"

PORT = int(getenv('APP_PORT', '3000'))
HOST = getenv('APP_HOST')

DATABASE_URL = getenv('DATABASE_URL')
DATABASE_NAME = getenv('DATABASE_NAME')
DATABASE_POOL_SIZE = int(getenv('DATABASE_POOL_SIZE'))
ADMIN_AUTH_USERNAME = getenv('ADMIN_AUTH_USERNAME')
ADMIN_AUTH_PASSWORD = getenv('ADMIN_AUTH_PASSWORD')