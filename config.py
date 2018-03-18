import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False # Turns on debugging features in Flask
    BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension
    MAIL_FROM_EMAIL = "sven@musmehl.de" # For use in application emails
    BOOTSTRAP_SERVE_LOCAL = True # forces flask-bootstrap to use local bootstrap resources
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
