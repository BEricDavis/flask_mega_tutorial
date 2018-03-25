import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # used to sign cookies etc.  Flask-WTF uses it to protect against CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLAlchemy parameters
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Email config for error handling
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['feralmonkey@gmail.com']
    # Pagination settings
    POSTS_PER_PAGE = 3
    # Languages to handle in flask-babel
    LANGUAGES = ['en', 'es']
    # Azure text translate key
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')