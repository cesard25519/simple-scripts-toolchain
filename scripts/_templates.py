from secrets import token_hex


dot_env_pg: str = f'''
DATABASE_DATABASE=sample
DATABASE_PASSWORD=admin
DATABASE_HOST=localhost
DATABASE_USER=admin
DATABASE_PORT=5432
DATABASE_MAX=4

HOST=localhost
PORT=1000
DEBUG=1

TOKEN_KEY_EXPIRE_TIME=600
TOKEN_KEY="{ token_hex(32) }"
'''

