import os
#from flask_script import Manager
#from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from backend import app, db
from models import Spot, TimestampChange, Average

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()