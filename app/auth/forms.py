from flask_wtf import FlaskForm
from ..models import User
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms_components import ColorField
from wtforms.validators import DataRequired, EqualTo, Length, Email, Regexp, ValidationError

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
        "Username must have only letters, numbers, dots or unserscores")])

    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("Log In")


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
        "Username must have only letters, numbers, dots or unserscores")])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Confirm password", validators=[
        DataRequired(),
        EqualTo("password", message="Passwords must match")])

    register_key = StringField("Secret key", validators=[DataRequired()])
    color = ColorField()
    submit = SubmitField("Register")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in use.")