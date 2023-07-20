from flask import Blueprint, render_template
# Everything that the users have access to is stored in this file

# Setting up a blueprint for flask application
views = Blueprint('views', __name__)

# defines the homepage by using the URL
@views.route('/')
def home():
    return render_template("home.html")




