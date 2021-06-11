#! /usr/bin/python3
from app import create_app, db # from app __init__
# initialize our extension & serve class help us launch out server
from flask_script import Manager, Server
from app.models import User, Role , Review
from flask_migrate import Migrate, MigrateCommand

# create app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
# we have used the manage decorator to create a shell context..
@manager.shell
def make_shell_context():
  return dict(app = app, db = db, User = User, Role = Role)

migrate = Migrate(app, db) # intialze migrate pass in db and app instance
manager.add_command('db',MigrateCommand) #manager command and pass the migratecommand class

if __name__ == '__main__':
  manager.run()
