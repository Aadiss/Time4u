import re
from flask import render_template, redirect, url_for, request, Blueprint
from flask_login import current_user

views_bp = Blueprint("views", __name__)

@views_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pass
    else:
        return render_template("index.html", user=current_user)