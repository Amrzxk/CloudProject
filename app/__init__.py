from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, 
                template_folder='interfaces/templates',
                static_folder='interfaces/static')
    
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-for-testing')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///vehicleservice.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    with app.app_context():
        # Import models and repositories
        from app.infrastructure.persistence.models.db_models import User
        
        # Import and register blueprints
        from app.interfaces.routes.auth import auth
        from app.interfaces.routes.user import user
        from app.interfaces.routes.mechanic import mechanic
        from app.interfaces.routes.main import main
        
        app.register_blueprint(auth)
        app.register_blueprint(user)
        app.register_blueprint(mechanic)
        app.register_blueprint(main)
        
        # Create database tables
        db.create_all()
        
    return app 