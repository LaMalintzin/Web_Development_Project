from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# This file makes it possible for all the other files to access eachother

# Creating a simple database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    # Important to keep secret, but this is just demo project. 
    app.config['SECRET_KEY'] = 'xxxxx xxxxx xxxxx xxxxx'
    # Make flask aware of we are using a database to store data and where this file is located
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    # Register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Script to check if the database is running correctly
    from .models import User, Note
    
    #create_database(app)
    
    with app.app_context():  # Enter the application context before creating the database
        create_database(app)
    
    return app

# Function which checks if the database exist, if not it will be created.
# Important to do this check so we dont overwrite an existing DB.
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print('Created Database!')

