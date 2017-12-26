import os

class Config(object):
    # used to sign cookies etc.  Flask-WTF uses it to protect against CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'