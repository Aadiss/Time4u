from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_NAME = "postgresql://postgres:qaz@localhost/time4u"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "qazwsxedc"
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_NAME
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views_bp

    app.register_blueprint(views_bp, url_prefix="/")

    return app