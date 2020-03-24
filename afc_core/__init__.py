import os
from flask import Flask

APP_ROOT = os.path.join(os.path.dirname(__file__))


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../afc_dev.db'
    app.url_map.strict_slashes = False

    from afc_core.user.controller import user

    app.register_blueprint(user, url_prefix='/api/user')

    return app


app = create_app()
