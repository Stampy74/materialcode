from app import app
from app import app, db
from app.models import User, Post

# Allow running of flask shell at the terminal to load imports
@app.shell_context_processor
def make_shell_context():
    return{'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    app.run(debug=True)





