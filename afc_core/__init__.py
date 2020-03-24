import os
from flask import Flask

APP_ROOT = os.path.join(os.path.dirname(__file__))


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../afc_dev.db'
    app.url_map.strict_slashes = False

    return app


app = create_app()
