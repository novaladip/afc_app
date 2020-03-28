import os
from pathlib import Path
from flask import Flask

from .manage import ma, jwt
from afc_core.models import db

APP_ROOT = os.path.join(os.path.dirname(__file__))
UPLOAD_FOLDER = Path(__file__).parent.parent.__str__() + '/upload/avatar'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../afc_dev.db'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['JWT_SECRET_KEY'] = 'N0tL0v1ng1sh4rderth_an_u_know'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.url_map.strict_slashes = False
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    # User API
    from afc_core.api.user.controller import user
    app.register_blueprint(user, url_prefix='/api/user')

    # Course API
    from afc_core.api.course.controller import course
    app.register_blueprint(course, url_prefix='/api/course')

    # Enrollment API
    from afc_core.api.enrollment.controller import enrollment
    app.register_blueprint(enrollment, url_prefix='/api/enrollment')

    # Section API
    from afc_core.api.section.controller import section
    app.register_blueprint(section, url_prefix='/api/section')

    # Attendance API
    from afc_core.api.attendance.controller import attendance
    app.register_blueprint(attendance, url_prefix='/api/attendance')

    return app


app = create_app()
