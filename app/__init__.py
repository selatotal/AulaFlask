from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .talks import talks as talks_blueprint
    app.register_blueprint(talks_blueprint)

    # Inicializando app Bootstrap
    bootstrap(app)

    return app

