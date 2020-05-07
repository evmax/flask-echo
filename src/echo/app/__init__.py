from flask import Flask

from .config import configure


app = Flask(__name__)
application = app  # gunicorn

configure(app)


from echo.app.api import base
from echo.app.api import routes
from echo.app.logger import configure_logging

configure_logging(app.config['DEBUG'])
