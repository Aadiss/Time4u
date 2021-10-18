import re
from flask import render_template, redirect, url_for, request, Blueprint
from flask.helpers import flash
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Task
from . import db

views_bp = Blueprint("views", __name__)

AVAILABLE_STATUS = ['To Do', 'In Development', 'In Analysis', 'Done']

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

        #edit form for rasks
        edited_content = request.form.get("edit_content")
        status = request.form.get("status")
        edited_task_id = request.form.get("edit_id")

        print(edited_content, status, edited_task_id)

        if (username or email or password1 or password2) or (title or priority or subject or content or date_expired) or (edited_content or status or edited_task_id):
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
                
            if edited_content or status:
                edited_task = Task.query.filter_by(id=edited_task_id).first()
                if edited_content:
                    edited_task.content = edited_content
                if status not in AVAILABLE_STATUS:
                    flash("Invalid status!", category="error")
                    return redirect(url_for("views.home"))
                else:
                    edited_task.status = status

                db.session.commit()
                flash("Edited successfuly", category="success")
                return redirect(url_for("views.home"))
            else:
                flash("Fill all fields!", category="error")
                return redirect(url_for("views.home"))
        else:
            flash("Fill all fields!", category="error")
            return redirect(url_for("views.home"))
            
    else:
        if current_user.is_authenticated:
            tasks = Task.query.filter_by(owner=current_user.id).order_by(Task.date_expired).all()
            return render_template("index.html", user=current_user, tasks=tasks)
        else:
            return render_template("index.html", user=current_user)