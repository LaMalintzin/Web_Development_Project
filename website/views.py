from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Everything that the users have access to is stored in this file
# Setting up a blueprint for flask application
views = Blueprint('views', __name__)

# defines the homepage by using the URL
@views.route('/')
@login_required
def home():
    return render_template("home.html", user = current_user)




