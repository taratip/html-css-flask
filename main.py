from app import app, db
from app.models import Role, User


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Role': Role, 'User': User}
