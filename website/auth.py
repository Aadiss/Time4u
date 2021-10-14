from flask import render_template, redirect, url_for, request, Blueprint
from flask.helpers import flash
from flask_login import current_user, logout_user, login_required, login_user
from werkzeug.security import check_password_hash
from .models import User

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
                flash("Login successful", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
         

    else:
        return render_template("login.html", user=current_user)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))