from myweb import app
from flask.ext.script import Manager

if __name__ == '__main__':
    manager = Manager(app)
    manager.run()