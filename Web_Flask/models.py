from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

db = SQLAlchemy()
meta = MetaData()

## Client DB Model
class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255), unique=True, nullable=False)
    lastName = db.Column(db.String(255), unique=True, nullable=False)
    
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def __repr__(self):
        return '<Clients %r>' % self.firstName