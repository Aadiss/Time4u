import re
from flask import render_template, redirect, url_for, request, Blueprint
from flask.helpers import flash
from flask_login import current_user
from .models import User

views_bp = Blueprint("views", __name__)

@views_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_in_db = User.query.filter_by(email=email).first()
        username_in_db = User.query.filter_by(login=username).first()

        if not username or not email or not password1 or not password2:
            flash("Fill all fields!", category="error")
            return redirect(url_for("views.home"))
        elif email_in_db:
            flash("Email already exists!", category="error")
            return redirect(url_for("views.home"))
        elif username_in_db:
            flash("Username already exist!", category="error")
            return redirect(url_for("views.home"))
        elif "@" not in email:
            flash("Invalid email!", category="error")
            return redirect(url_for("views.home"))
        elif len(username) < 6:
            flash("Usarname must be at least 6 signs!", category="error")
            return redirect(url_for("views.home"))
        elif len(password1) < 6:
            flash("Password must be at least 6 signs!", category="error")
            return redirect(url_for("views.home"))
        elif password1 != password2:
            flash("Passwords do not match!", category="error")
            return redirect(url_for("views.home"))
        else:
            pass

        print(username, email, password1, password2)
        flash("Success!", category="success")
        return redirect(url_for("views.home"))
    else:
        return render_template("index.html", user=current_user)