from flask import Flask

def create_app():
    app = Flask(__name__)
    # Important to keep secret, but this is just demo project. 
    app.config['SECRET_KEY'] = 'xxxxx xxxxx xxxxx xxxxx'

    return app

