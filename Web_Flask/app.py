#Imports
from enum import unique
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
#from models import Client
import csv

#Configure Flask
app = Flask(__name__)

# DB Connection
db_name = "sqlite_database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#db will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

## Client DB Model
class clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), unique=True, nullable=False)
    lastname = db.Column(db.String(255), unique=True, nullable=False)
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        db.session.commit()


@app.route("/")
def index():
    return render_template("index.html")


#TODO link this to database
@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("firstName") or not request.form.get("lastName"):
        return render_template("failure.html")
    file = open("registered.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("firstName"), request.form.get("lastName")))
    
    
    
    return render_template("success.html")


@app.route("/registered_clients")
def registered_clients():
    return render_template("registered.html", clients=clients.query.all())

# __name__ is set to __main__ at runtime when running app directly
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)