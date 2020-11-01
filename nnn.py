from app import create_app, db
from flask_migrate import Migrate

app = create_app("development")

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return { "db":db }