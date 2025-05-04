from app import db
from app.domain.models.models import ServiceRequest, Vehicle, ServiceType
from datetime import datetime
from flask_login import current_user

class ServiceRequestService:
    @staticmethod
    def create_vehicle(type, make, model, year, license_plate):
        """Create a new vehicle"""
        new_vehicle = Vehicle(
            type=type,
            make=make, 
            model=model,
            year=year,
            license_plate=license_plate
        )
        
        db.session.add(new_vehicle)
        db.session.commit()
        
        return new_vehicle
    
    @staticmethod
    def get_service_types():
        """Get all service types"""
        return ServiceType.query.all()
    
    @staticmethod
    def create_service_request(user_id, vehicle_id, service_type_id, requested_date, notes=None):
        """Create a new service request"""
        new_request = ServiceRequest(
            user_id=user_id,
            vehicle_id=vehicle_id,
            service_type_id=service_type_id,
            requested_date=requested_date,
            notes=notes,
            status='pending'
        )
        
        db.session.add(new_request)
        db.session.commit()
        
        return new_request
    
    @staticmethod
    def get_user_requests(user_id):
        """Get service requests for a specific user"""
        return ServiceRequest.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_pending_requests():
        """Get all pending service requests for mechanics"""
        return ServiceRequest.query.filter_by(status='pending').all()
    
    @staticmethod
    def get_mechanic_requests(mechanic_id):
        """Get service requests assigned to a specific mechanic"""
        return ServiceRequest.query.filter_by(mechanic_id=mechanic_id).all()
    
    @staticmethod
    def update_request_status(request_id, status, mechanic_id=None):
        """Update the status of a service request"""
        request = ServiceRequest.query.get(request_id)
        
        if not request:
            return False, "Service request not found"
        
        request.status = status
        
        if mechanic_id and status == 'accepted':
            request.mechanic_id = mechanic_id
        
        db.session.commit()
        
        return True, f"Service request {status}"
    
    @staticmethod
    def delete_request(request_id):
        """Delete a service request from the database"""
        request = ServiceRequest.query.get(request_id)
        if not request:
            return False, "Service request not found"
        db.session.delete(request)
        db.session.commit()
        return True, "Service request deleted successfully" 