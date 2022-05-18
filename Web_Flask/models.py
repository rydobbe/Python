# Imports
from pickle import TRUE
from unittest.util import _MAX_LENGTH
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class Client(db.Model):
    __tablename__ = "Client"
    id = db.Column(db.Integer(), primary_key=True)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(255), unique=True ,nullable=False)
    phone = db.Column(db.Integer(), nullable=False)
    socialSecurity = db.Column(db.Integer(), _MAX_LENGTH=9, unique=True ,nullable=False)
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