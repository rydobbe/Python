#Imports
from enum import unique
from re import M
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from models import Clients
import csv

#Configure Flask
app = Flask(__name__)
app.secret_key = "hehehe"

# DB Connection
db_name = "sqlite_database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#db will be used for all SQLAlchemy commands
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=['POST'])
def register():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    client = Clients(firstName=firstName, lastName=lastName)
    db.session.add(client)
    db.session.commit()
    return redirect(url_for("registered_clients"))


@app.route("/registered_clients")
def registered_clients():
    return render_template("registered.html", clients=Clients.query.all())

# __name__ is set to __main__ at runtime when running app directly
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)