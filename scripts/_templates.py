from secrets import token_hex

__dotenv: list[str] = [
    'HOST="0.0.0.0"',
    'PORT=4000',
    'DEBUG=1',

    'TOKEN_KEY_EXPIRE_TIME=600',
    f'TOKEN_KEY={ token_hex(32) }',
]

__turso_env_vars: list[str] = [
    'DATABASE_URL="zample.db"',
    'DATABASE_AUTH_TOKEN="...?"',
]
__pg_env_vars: list[str] = [
    'DATABASE_PASSWORD=admin',
    'DATABASE_HOST=localhost',
    'DATABASE_NAME=sample',
    'DATABASE_USER=admin',
    'DATABASE_PORT=5432',
    'DATABASE_MAX=4',
]

dotenv_pg: str = '\n'.join( __dotenv + __pg_env_vars )

dotenv: str = '\n'.join( __dotenv + __turso_env_vars )

blank_py: str = """
def main() -> None:
    ...


if __name__ == '__main__':
    main()
"""
