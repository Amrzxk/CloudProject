from app.infrastructure.persistence.models.db_models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user

class AuthService:
    @staticmethod
    def register(username, email, password, role='user'):
        """Register a new user"""
        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return False, "Username already exists"
        
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            return False, "Email already exists"
        
        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password, role=role)
        
        db.session.add(new_user)
        db.session.commit()
        
        return True, "User created successfully"
    
    @staticmethod
    def login(username, password):
        """Login a user"""
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password, password):
            return False, "Invalid username or password"
        
        login_user(user)
        return True, "Login successful"
    
    @staticmethod
    def logout():
        """Logout a user"""
        logout_user()
        return True, "Logout successful" 