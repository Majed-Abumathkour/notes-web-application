from flask import Flask
from website.views import views
from .auth import auth


def create_app():
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.config["SECRET_KEY"] = "asdf asdf asdf"
    return app