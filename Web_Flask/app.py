#Imports
from enum import unique
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


#Configure Flask
app = Flask(__name__)
app.secret_key = "hehehe"

# DB Connection/Config
db_name = "sqlite_database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# DB will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# DB Model
class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def __repr__(self):
        return '<Clients %r>' % self.firstName


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


@app.route("/drop", methods=['POST'])
def drop():
    db.drop_all()
    db.session.commit()
    return redirect(url_for("index"))


# __name__ is set to __main__ at runtime when running app directly
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)