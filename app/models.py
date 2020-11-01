from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    _password_hash = db.Column(db.String(200))

    @property
    def password(self):
        return AttributeError("this property is inaccesible.")

    @password.setter
    def password(self, password):
        self._password_hash = generate_password_hash(password, salt_length=32)
    
    def verify_password(self, password):
        return check_password_hash(self._password_hash, password)


    def __repr__(self):
        return f"<ModelName: {self.username}>"