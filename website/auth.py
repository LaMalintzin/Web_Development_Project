from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

#Define login, logout and sign-up
@auth.route('/login')
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
