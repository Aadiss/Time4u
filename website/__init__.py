from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

DB_NAME = "postgres://tqykwvgzcrxbck:4fe8b54617792dbea8d5e2e88992df30191d67cfec9b24dbba094cf405baadb1@ec2-34-249-247-7.eu-west-1.compute.amazonaws.com:5432/d8ne3r3rnot6gk"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "qazwsxedc"
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_NAME
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views_bp
    from .auth import auth_bp
    from .models import User

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    app.register_blueprint(views_bp, url_prefix="/")
    app.register_blueprint(auth_bp, url_prefix="/")

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app