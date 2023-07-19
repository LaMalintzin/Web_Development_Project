from flask import Blueprint
# Everything that the users have access to is stored in this file

# Setting up a blueprint for flask application
views = Blueprint('views', __name__)

# defines the homepage by using the URL
@views.route('/')
def home():
    return "<h1>Test</h1>"




