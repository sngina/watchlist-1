from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig # for devconfig

app = Flask(__name__,instance_relative_config = True) # app instance

# setting up configuration
app.config.from_object(DevConfig) # method to set up configuration and pass in the DevConfig subclass.
app.config.from_pyfile('config.py')

# initializing flask extensions
bootstrap = Bootstrap(app)

from app import views # view from inside the app
from app import error
