template_flaskenv: str = """FLASK_APP=app
FLASK_DEBUG=1
"""

template_app_ini: str = """from os import makedirs

from dotenv import load_dotenv, dotenv_values; load_dotenv()
from flask import Flask


def create_app() -> Flask:
    app: Flask = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(dotenv_values())

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
