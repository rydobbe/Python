#Imports
from datetime import date
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

# # DB Model
class Client(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.Integer(), nullable=False)
    socialSecurity = db.Column(db.Integer(), nullable=False)
    dateOfBirth = db.Column(db.Integer(), nullable=False)
    annualIncome = db.Column(db.Integer(), nullable=False)
    monthlyRent = db.Column(db.Integer(), nullable=False)
    zipCode = db.Column(db.Integer(), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    

    
    def __init__(self, firstName, lastName, address, city,
                        state, email, phone, socialSecurity,
                        dateOfBirth, annualIncome, monthlyRent,
                        zipCode, country):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.city = city
        self.state = state
        self.email = email
        self.phone = phone
        self.socialSecurity = socialSecurity
        self.dateOfBirth = dateOfBirth
        self.annualIncome = annualIncome
        self.monthlyRent = monthlyRent
        self.zipCode = zipCode
        self.country = country


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=['POST'])
def register():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    email = request.form['email']
    phone = request.form['phone']
    socialSecurity = request.form['socialSecurity']
    dateOfBirth = request.form['dateOfBirth']
    annualIncome = request.form['annualIncome']
    monthlyRent = request.form['monthlyRent']
    zipCode = request.form['zipCode']
    country = request.form['country']
    client = Client(firstName=firstName, lastName=lastName, address=address,
                    city=city, state=state, email=email, phone=phone,
                    socialSecurity=socialSecurity, dateOfBirth=dateOfBirth,
                    annualIncome=annualIncome, monthlyRent=monthlyRent, zipCode=zipCode,
                    country=country)
    db.session.add(client)
    db.session.commit()
    return redirect(url_for("registered_clients"))


@app.route("/registered_clients")
def registered_clients():
    return render_template("registered.html", clients=Client.query.all())


@app.route("/view_clients", methods=['POST'])
def view_clients():
    return redirect(url_for("registered_clients"))

@app.route("/drop", methods=['POST'])
def drop():
    db.drop_all()
    db.create_all()
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/add", methods=['POST'])
def add():
    return redirect(url_for("index"))

@app.route("/client_view")
def client_view():
    return render_template("client_view.html")

# __name__ is set to __main__ at runtime when running app directly
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)