from time import time
from flask import render_template, redirect, url_for, request, Blueprint
from flask.helpers import flash
from flask_login import current_user, logout_user, login_required, login_user
from sqlalchemy.sql.functions import current_date, user
from werkzeug.security import check_password_hash
from sqlalchemy.sql import func
from .models import User, Task
from . import db
from datetime import datetime, date, timedelta

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("email")
        password = request.form.get("password1")

        if not username or not password:
            flash("Fill all fields!", category="error")
            return redirect(url_for("auth.login"))
        else:
            if '@' in username:
                user = User.query.filter_by(email=username).first()
            else:
                user = User.query.filter_by(login=username).first()
            
            if not user:
                flash("Invalid username or password!", category="error")
                return redirect(url_for("auth.login"))
            elif not check_password_hash(user.password, password):
                flash("Invalid username or password!", category="error")
                return redirect(url_for("auth.login"))
            else:
                user.last_time_active = func.now()
                db.session.commit()
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
         

    else:
        return render_template("login.html", user=current_user)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout succesfull!", category="success")
    return redirect(url_for("auth.login"))


@auth_bp.route("/condition/<int:condition_id>")
@login_required
def condition(condition_id: int):
    if condition_id == 1:
        deadline_day = date.today() + timedelta(days=5)
        print(deadline_day)
        tasks = Task.query.filter(Task.owner == current_user.id, Task.status != "Done", Task.date_expired <= deadline_day, Task.date_expired >= date.today() ).order_by(Task.date_expired).all()
        return render_template("condition.html", user=current_user, tasks=tasks)
    elif condition_id == 2:
        return render_template("condition.html", user=current_user)
    elif condition_id == 3:
        tasks = Task.query.filter_by(owner=current_user.id, status="Done").order_by(Task.date_expired).all()
    elif condition_id == 4:
        tasks = Task.query.filter_by(owner=current_user.id, status="In Development").order_by(Task.date_expired).all()
    elif condition_id == 5:
        tasks = Task.query.filter_by(owner=current_user.id, status="To Do").order_by(Task.date_expired).all()
    else:
        tasks = Task.query.filter_by(owner=current_user.id).order_by(Task.date_expired).all()
    return render_template("condition.html", user=current_user, tasks=tasks)