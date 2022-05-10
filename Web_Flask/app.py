#Imports
from flask import Flask, render_template, request
import csv

#Configure Flask
app = Flask(__name__)

#Registered Clients
clients = []

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