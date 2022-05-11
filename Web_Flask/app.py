#Imports
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import csv
import os

#Configure Flask
app = Flask(__name__)

# DB Connection
db_name = "sqlite_database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#db will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

##Registered Clients
# clients = []


##Test db connection
# @app.route("/")
# def testdb():
#     try:
#         db.session.query(text('1')).from_statement(text('SELECT 1')).all()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         # e is the description of the error
#         error_text = "<p>The error:<br>" + str(e) + "<p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text


@app.route("/")
def index():
    return render_template("index.html")


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
    with open("registered.csv", "r") as file:
        reader = csv.reader(file)
        clients = list(reader)
    return render_template("registered.html", clients=clients)

# __name__ is set to __main__ at runtime when running app directly
if __name__ == '__main__':
    app.run(debug=True)