from flask import Flask

def create_app():
    app = Flask(__name__)
    # Important to keep secret, but this is just demo project. 
    app.config['SECRET_KEY'] = 'xxxxx xxxxx xxxxx xxxxx'

    from .views import views
    from .auth import auth

    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

