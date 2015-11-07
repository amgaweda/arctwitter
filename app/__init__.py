import os

from flask import Flask
import config
import logging
from logging import StreamHandler

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, static_folder='static', static_url_path='')

file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
app.logger.addHandler(file_handler)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

app.config.from_pyfile('../config.py')
#from flask_sslify import SSLify
#if 'DYNO' in os.environ: # only trigger SSLify if the app is running on Heroku
#	sslify = SSLify(app)

app.config["MAIL_SERVER"] 	= "smtp.gmail.com"
app.config["MAIL_PORT"] 	= 465
app.config["MAIL_USE_SSL"] 	= True
app.config["MAIL_USERNAME"] = 'contact@example.com'
app.config["MAIL_PASSWORD"] = 'your-password'

from app import views

