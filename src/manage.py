#!flask/bin/python
from flask_script import Manager
from echo.app import app

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
