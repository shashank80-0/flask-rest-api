"""Runs Flask App and enables API."""


from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:shashank@123@localhost:3306/store_db'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'myauth'

if __name__ == '__main__':
    from views import *
    app.run(debug=True)