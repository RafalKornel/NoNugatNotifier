from . import db

class ModelName(db.Model):
    __tablename__ = "model_name"

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"<ModelName: {self}>"