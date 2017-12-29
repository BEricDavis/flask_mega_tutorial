from app import app, db
from app.models import User, Post

# create a shell context for the 'flask shell' command
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}