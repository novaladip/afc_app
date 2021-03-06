"""
These are commands to flask-migrate
python manage.py db init --> init migrations
python manage.py db migrate --> migrate models
python manage.py db upgrade --> apply changes
python manage.py db --help --> :)
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from afc_core import app
from afc_core.models import db
from afc_core.models.user import User
from afc_core.models.course import Course
# from afc_core.models.section import Section
# from afc_core.models.attendance import Attendance
# from afc_core.models.enrollment import Enrollment


db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
