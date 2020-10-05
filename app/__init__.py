from flask import Flask
from flask_cors import CORS

app = None


def create_app(env):
    """Construct the core application."""
    global app
    app = Flask(__name__, template_folder='../web/templates', static_folder='../web/static',
                instance_relative_config=False)
    CORS(app)
    from config import config
    config = config.ConfigLoader().get_config(env)
    app.config['config'] = config

    with app.app_context():
        from . import routes
        return app


def get_app():
    if not app:
        raise Exception('application is still not initialized')
    return app
