from . import db 
from flask_login import UserMixin

#let alchemy handle the date 
from sqlalchemy.sql import func

# creating a schema
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    # remember to capitalize the first letter of the linked attribute 
    notes = db.relationship('Note')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10_000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    # foreign key linking
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

