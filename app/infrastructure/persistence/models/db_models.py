from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), default='user')  # 'user' or 'mechanic'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    service_requests = db.relationship('ServiceRequest', 
                                      foreign_keys='ServiceRequest.user_id',
                                      backref='customer', lazy=True)
    assigned_service_requests = db.relationship('ServiceRequest',
                                              foreign_keys='ServiceRequest.mechanic_id',
                                              backref='mechanic', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)  # 'car' or 'bike'
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    license_plate = db.Column(db.String(20), nullable=False)
    
    # Relationships
    service_requests = db.relationship('ServiceRequest', backref='vehicle', lazy=True)
    
    def __repr__(self):
        return f'<Vehicle {self.make} {self.model} ({self.license_plate})>'

class ServiceType(db.Model):
    __tablename__ = 'service_types'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # Relationships
    service_requests = db.relationship('ServiceRequest', backref='service_type', lazy=True)
    
    def __repr__(self):
        return f'<ServiceType {self.name}>'

class ServiceRequest(db.Model):
    __tablename__ = 'service_requests'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    service_type_id = db.Column(db.Integer, db.ForeignKey('service_types.id'), nullable=False)
    mechanic_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'accepted', 'in_progress', 'completed', 'rejected'
    requested_date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<ServiceRequest {self.id} - {self.status}>' 