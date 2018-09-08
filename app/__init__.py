from flask import Flask
from flask_login import LoginManager

from app.model.book import db

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.app')
    app.config.from_object('config.database')
    register_buleprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()

    return app


def register_buleprint(app):
    from app.web.book import web
    app.register_blueprint(web)
