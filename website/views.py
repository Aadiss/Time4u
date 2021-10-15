import re
from flask import render_template, redirect, url_for, request, Blueprint
from flask.helpers import flash
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Task
from . import db

views_bp = Blueprint("views", __name__)

@views_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # register form
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        #popup form for tasks
        title = request.form.get("title")
        priority = request.form.get("priority")
        subject = request.form.get("subject")
        content = request.form.get("content")
        date_expired = request.form.get("date-expired")

        if (username or email or password1 or password2) or (title or priority or subject or content or date_expired):
            if username and email and password1 and password2:
                email_in_db = User.query.filter_by(email=email).first()
                username_in_db = User.query.filter_by(login=username).first()

                if email_in_db:
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
                    new_user = User(email=email, login=username, password = generate_password_hash(password1, method="sha256"))
                    db.session.add(new_user)
                    db.session.commit()
                    print("user createt")
                    login_user(new_user, remember=True)
                    flash("Registration complete!", category="success")
                    return redirect(url_for("views.home"))
            
            if title and priority and subject and content and date_expired:
                new_task = Task(title=title, priority=priority, subject=subject, content=content, date_expired=date_expired, owner=current_user.id)
                db.session.add(new_task)
                db.session.commit()
                flash("Added successfuly", category="success")
                return redirect(url_for("views.home"))
            else:
                flash("Fill all fields!", category="error")
                return redirect(url_for("views.home"))
        else:
            flash("Fill all fields!", category="error")
            return redirect(url_for("views.home"))
            
    else:
        return render_template("index.html", user=current_user)