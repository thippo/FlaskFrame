from flask import Flask, redirect
import config
from . import home, errors, bitcoin, test

app = Flask(__name__)
#app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config.config['default'])
#app.config.from_pyfile('config.py')
#app.config.from_envvar('APP_CONFIG_FILE')
app.config['SECRET_KEY'] = 'abc' 

def register(blueprints):
    for i in blueprints:
        app.register_blueprint(i)

@app.route('/')
def index():
    return redirect('/home')

register(home.blueprints)
register(errors.blueprints)
register(bitcoin.blueprints)
register(test.blueprints)