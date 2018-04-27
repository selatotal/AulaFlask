from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .talks import talks as talks_blueprint
    app.register_blueprint(talks_blueprint)

    # Inicializando app Bootstrap
    bootstrap(app)

    # Inicializando Database
    db.init_app(app)

    # Inicializando Autenticacao
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app



