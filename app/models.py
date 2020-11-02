from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    _password_hash = db.Column(db.String(200))
    color = db.Column(db.String(16), default="#000000")
    failed = db.Column(db.Boolean, default=False)
    date_of_failure = db.Column(db.Date)
    last_seen = db.Column(db.Date)
    answered_today = db.Column(db.Boolean, default=False)
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))

    @property
    def password(self):
        return AttributeError("this property is inaccesible.")

    @password.setter
    def password(self, password):
        self._password_hash = generate_password_hash(password, salt_length=32)
    
    def verify_password(self, password):
        return check_password_hash(self._password_hash, password)

    
    def seen_today(self):
        return self.last_seen == date.today()

    def __repr__(self):
        return f"<User: {self.username} | failed: {self.failed} {self.date_of_failure} |\
             answered_today: {self.answered_today} | last_seen: {self.last_seen}\
                  | color: {self.color} | group: {self.group}>"

class Group(db.Model):
    __tablename__ = "groups"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    key = db.Column(db.String(64))
    users = db.relationship("User", backref="group")

    def __repr__(self):
        return f"<Group {self.name}>"