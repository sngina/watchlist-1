#! /usr/bin/python3
from app import create_app # from app __init__
# initialize our extension & serve class help us launch out server
from flask_script import Manager, Server

# create app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
  manager.run()
