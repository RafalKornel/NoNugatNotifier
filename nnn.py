from app import create_app, db
from app.models import User, Group
from flask_migrate import Migrate

app = create_app("development")

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return { "db":db, "User":User, "Group":Group }

@app.cli.command("create_tables")
def create_tables():
    db.create_all()

@app.cli.command("drop_tables")
def drop_tables():
    db.drop_all()