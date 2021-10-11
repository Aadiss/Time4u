from flask import render_template, redirect, url_for, request, Blueprint

views_bp = Blueprint("views", __name__)

@views_bp.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")