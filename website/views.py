import re
from flask import render_template, redirect, url_for, request, Blueprint
from flask.helpers import flash
from flask_login import current_user

views_bp = Blueprint("views", __name__)

@views_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        print(username, email, password1, password2)
        flash("Success!", category="success")
        return redirect(url_for("views.home"))
    else:
        return render_template("index.html", user=current_user)