from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

DB_NAME = "postgresql://postgres:qaz@localhost/time4u"

app = Flask(__name__)
app.config["SECRET_KEY"] = "qazwsxedc"
app.config["SQLALCHEMY_DATABASE_URI"] = DB_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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
