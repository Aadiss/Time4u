from sqlalchemy.orm import defaultload
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    login = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    last_time_active = db.Column(db.DateTime(timezone=True), default=func.now())

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    priority = db.Column(db.String(50))
    subject = db.Column(db.String(100), nullable=True)
    content = db.Column(db.String(400))
    status = db.Column(db.String(50), default="To Do")
    is_closed = db.Column(db.String(2), default='N')
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    date_expired = db.Column(db.DateTime(timezone=True), nullable=True)
    owner = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)