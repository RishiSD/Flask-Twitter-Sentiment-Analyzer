from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from TwitApp.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from TwitApp.routes import tweet
    app.register_blueprint(tweet)

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app
