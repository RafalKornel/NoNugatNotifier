from flask_login.utils import login_required
from . import main
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import date
from .forms import QuestionForm
from .. import db
from ..models import User

@main.route("/")
def index():
    if not current_user.is_authenticated:
        return render_template("index.html")
    else: 
        if not current_user.seen_today():
            current_user.answered_today = False
            return redirect(url_for("main.question"))
        else:
            return redirect(url_for("main.calendar"))

@main.route("/calendar")
@login_required
def calendar():
    if not current_user.answered_today: 
        return redirect(url_for("main.question"))
    return render_template(
        "calendar.html", 
        users=User.query.filter_by(group=current_user.group))


@main.route("/question", methods=["GET", "POST"])
@login_required
def question():

    if current_user.answered_today: 
        flash("Already answered today.")
        return redirect(url_for(
            "main.calendar"), 
            users=User.query.filter_by(group=current_user.group))

    if current_user.failed:
        flash("Sorry, you failed.")
        return redirect(url_for(
            "main.calendar"), 
            users=User.query.filter_by(group=current_user.group))

    form = QuestionForm()
    if form.validate_on_submit():
        answer = True if form.answer.data == "yes" else False

        if answer:
            current_user.date_of_failure = date.today()

        current_user.failed = answer
        current_user.answered_today = True
        current_user.last_seen = date.today()

        db.session.add(current_user)
        db.session.commit()

        return redirect(url_for("main.calendar"))


    return render_template( "question.html", form=form )