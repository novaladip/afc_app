import os
from pathlib import Path
from flask import Flask

from afc_core.models import db

APP_ROOT = os.path.join(os.path.dirname(__file__))
UPLOAD_FOLDER = Path(__file__).parent.parent.__str__() + '/upload/avatar'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../afc_dev.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.url_map.strict_slashes = False
    db.init_app(app)

    # User API
    from afc_core.user.controller import user
    app.register_blueprint(user, url_prefix='/api/user')

    return app


app = create_app()
