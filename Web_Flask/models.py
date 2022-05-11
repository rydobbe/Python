from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

db = SQLAlchemy()
meta = MetaData()

## Client DB Model
class clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), unique=True, nullable=False)
    lastname = db.Column(db.String(255), unique=True, nullable=False)
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname