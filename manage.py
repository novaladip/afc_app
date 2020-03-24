from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from afc_core import app
from afc_core.models import db
from afc_core.models.user import User

db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
