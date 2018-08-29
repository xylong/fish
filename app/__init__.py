from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.app')
    register_buleprint(app)
    return app

def register_buleprint(app):
    from app.web.book import web
    app.register_blueprint(web)