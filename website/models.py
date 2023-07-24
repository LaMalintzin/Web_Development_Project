from sqlalchemy import func
from website import db
from flask_login import UserMixin

# This file contains the database models

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # Creating a unique id for every user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

    # I added a property is_authenticated explicitly to the User class, even though it's already inherited through UserMixin. 
    # This will make it easier to understand the code and ensure the implementation is consistent.

    @property
    def is_authenticated(self):
        return True  # Assuming all users are authenticated

    @property
    def is_active(self):
        return True  # Assuming all users are active

    @property
    def is_anonymous(self):
        return False  # Assuming no users are anonymous

    def get_id(self):
        return str(self.id)  # Convert user ID to string for Flask-Login
