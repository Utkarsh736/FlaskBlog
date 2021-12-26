from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# __name__ is name of module (spl. var. in python)

app = Flask(__name__)

app.config['SECRET_KEY'] = '4d02ba5bcbaee679dd80e78cba5644b7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flaskblog import routes