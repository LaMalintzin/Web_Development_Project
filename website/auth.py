import dbm
from flask import Blueprint, render_template, request, flash, redirect, url_for

from website import DB_NAME
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint('auth', __name__)

#Define login, logout and sign-up
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be longer than 3 characters.', category='error')
        elif len (first_name) < 2:
            flash('First name must be longer than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords must match ', category='error')
        elif len(password1) < 7:
            flash('Password must be longer than 7 characters.', category='error')
        else:
            # Defining the user from models.py
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            # Add the newly created account to the database
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")
