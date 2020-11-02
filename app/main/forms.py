from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField

class QuestionForm(FlaskForm):
    answer = RadioField("Did you lose today?", choices=[("yes", "Yes"), ("no", "No")])
    submit = SubmitField("Submit")