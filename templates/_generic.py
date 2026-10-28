from secrets import token_hex


template_dotenv: str = f'''
HOST="0.0.0.0"
PORT=1000
DEBUG=1

DATABASE_URL="zample.db"
DATABASE_AUTH_TOKEN="...?"

TOKEN_KEY_EXPIRE_TIME=600
TOKEN_KEY="{ token_hex(32) }"
'''

template_main_file: str = """
def main() -> None:
    ...


if __name__ == '__main__':
    main()
"""
