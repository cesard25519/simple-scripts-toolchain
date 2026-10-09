template_dot_env: str = """DATABASE_URL=\"\"
"""

template_flaskenv: str = """FLASK_APP=app
FLASK_DEBUG=1
"""

template_app_ini: str = """from os import makedirs

from dotenv import load_dotenv, dotenv_values; load_dotenv()
from flask import Flask


def create_app(test_conf: bool = False) -> Flask:
    app: Flask = Flask(__name__, instance_relative_config=True)


    if test_conf: environ += '.debug'

    app.config.from_mapping(dotenv_values(environ))

    load_config(conf=app.config)
    register_paths(app=app)

    makedirs(app.instance_path, exist_ok=True)

    return app


def load_config(conf: dict) -> None:
    ...

def register_paths(app: Flask) -> None:
    # app.add_url_rule(rule='/', view_func=_.as_view(name=''))
    ...

"""
