from app import create_app, db
from app.models import User, Group
import click

app = create_app("development")

@app.shell_context_processor
def make_shell_context():
    return { "db":db, "User":User, "Group":Group }

@app.cli.command("create_tables")
def create_tables():
    db.create_all()

@app.cli.command("drop_tables")
def drop_tables():
    db.drop_all()

@app.cli.command("add_group")
@click.argument("group_name")
@click.argument("group_key")
def add_group(group_name, group_key):
    g = Group(name=group_name, key=group_key)
    db.session.add(g)
    db.session.commit()