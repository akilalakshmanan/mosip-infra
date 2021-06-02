import os

server = 'https://api-internal.sandbox.mosip.net'
ssl_verify=True

db_user = os.getenv('DB_USER')
db_pwd = os.getenv('DB_PWD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

superadmin_user = os.getenv('IAM_USERNAME') # With GLOBAL_ADMIN, ZONAL_ADMIN
superadmin_pwd =  os.getenv('IAM_PASSWORD')
