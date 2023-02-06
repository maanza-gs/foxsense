from flask import Flask
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI']='mongodb://localhost/thebookmark'
    mongo =  PyMongo(app)
    
    db = mongo.db.users

    CORS(app)
    
    from .auth import auth
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        pass

    if __name__ == '__main__':
        app.run(debug=True)