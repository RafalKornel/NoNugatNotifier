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
        return redirect(url_for("auth.login"))
    else: 
        if current_user.failed or current_user.seen_today():
            return redirect(url_for("main.calendar"))
        
        else:
            current_user.answered_today = False
            db.session.add(current_user)
            db.session.commit()
            return redirect(url_for("main.question"))


@main.route("/calendar")
@login_required
def calendar():
    if (not current_user.answered_today or not current_user.seen_today()) and not current_user.failed: 
        return redirect(url_for("main.question"))
    users = User.query.filter_by(group=current_user.group)
    users_calendar = { i: [] for i in range(1, 32) }
    for u in users:
        i = date.today().day if not u.failed else u.date_of_failure.day
        users_calendar[i].append(u)

    return render_template(
        "calendar.html", 
        users = User.query.filter_by(group=current_user.group).filter_by(failed=False),
        failed = User.query.filter_by(group=current_user.group).filter_by(failed=True),
        today = date.today().day,
        calendar = users_calendar)


@main.route("/question")
@login_required
def question():

    if current_user.answered_today or current_user.failed: 
        return redirect(url_for("main.calendar"))

    return render_template( "question.html" )


@main.route("/answer/<ans>")
@login_required
def answer(ans):

    if ans not in ["yes", "no"]:
        return redirect(url_for("main.question"))

    if current_user.answered_today:
        return redirect(url_for("main.calendar"))

    answer = (ans == "yes")

    if answer:
        current_user.date_of_failure = date.today()
    current_user.failed = answer
    current_user.answered_today = True
    current_user.last_seen = date.today()
    
    db.session.add(current_user)
    db.session.commit()
    
    return redirect(url_for("main.calendar"))