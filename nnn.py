from app import create_app, db
from app.models import User
from flask_migrate import Migrate

app = create_app("production")

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return { "db":db, "User":User }