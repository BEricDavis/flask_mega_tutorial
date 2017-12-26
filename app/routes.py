# routes.py - contains view functions
from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Eric'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful plumage!'
        },
        {
            'author': {'username': 'Susan'},
            'body': "It's an ex-parrot."
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)