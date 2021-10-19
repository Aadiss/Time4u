from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

DB_NAME = "postgres://bcxnapvkrnuxdm:6aee2e94f13fc111b03bc400b66dc67613a58503164c85d21a19962f0220e08b@ec2-52-209-171-51.eu-west-1.compute.amazonaws.com:5432/d2h3br7ted57l9"
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