import os


def _from_env(app):
    app.config['LOG_PATH'] = os.getenv('APP__LOG_PATH', '/var/log/')
    app.config['DEBUG'] = os.getenv('APP__DEBUG', False)


def configure(app):
    """."""
    path = os.environ.get('ECHO_SETTINGS_PATH')
    if path and os.path.exists(path):
        app.config.from_json(path)
    else:
        _from_env(app)
    app.config['JSON_AS_ASCII'] = False
