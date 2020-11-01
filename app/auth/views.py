from flask import render_template, request, redirect, url_for, flash, current_app
from flask_login.utils import login_required
from . import auth
from ..models import User
from .forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, current_user
from .. import db


@auth.route("/login", methods=["POST", "GET"])
def login():
    
    if current_user.is_authenticated:
        flash("Already logged in!")
        return redirect(url_for("main.index"))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data

        user = User.query.filter_by(username=username).first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get("next")
            if next is None or not next.startswith("/"):
                next = url_for("main.index")
            return redirect(next)
        flash("Invalid username or password")

    return render_template("auth/login.html", form=LoginForm())


@auth.route("/logout")
def logout():
    logout_user()
    flash("Succesfully logged out")
    return redirect(url_for("main.index"))


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit() and validate_secret_key(form.register_key.data):

        user = User(
            username = form.username.data,
            password = form.password.data,
        )

        db.session.add(user)
        db.session.commit()
        print(f"committed {user}")

        flash("Succesfully registered.")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)

def validate_secret_key(key):
    return current_app.config["REGISTER_KEY"] == key