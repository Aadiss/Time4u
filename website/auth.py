from flask import render_template, redirect, url_for, request, Blueprint
from flask_login import current_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        pass
    else:
        return render_template("login.html", user=current_user)