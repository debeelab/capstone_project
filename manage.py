from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


import app
from database.models import db

migrate = Migrate(app, db)
manager = Manager(app)


manager.add_command('db', Migrate)


if __name__ == '__main__':
    manager.run()
