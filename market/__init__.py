from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///../market/instance/market.db"
app.config['SECRET_KEY']='f86f524bcddb98dd23d951ed'
db = SQLAlchemy(app)

from market import routes