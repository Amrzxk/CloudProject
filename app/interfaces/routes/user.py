from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import login_required, current_user
from app.infrastructure.persistence.models.db_models import ServiceRequest, Vehicle, ServiceType
from app.application.services.service_request_service import ServiceRequestService
from datetime import datetime

user = Blueprint('user', __name__)

@user.route('/user/dashboard')
@login_required
def dashboard():
    """User dashboard route"""
    if current_user.role != 'user':
        return redirect(url_for('main.dashboard'))
    
    service_requests = ServiceRequestService.get_user_requests(current_user.id)
    return render_template('user/dashboard.html', service_requests=service_requests)

@user.route('/user/book-service', methods=['GET', 'POST'])
@login_required
def book_service():
    """Book service route"""
    if current_user.role != 'user':
        return redirect(url_for('main.dashboard'))
    
    service_types = ServiceRequestService.get_service_types()
    
    if request.method == 'POST':
        # Get form data
        vehicle_type = request.form.get('vehicle_type')
        make = request.form.get('make')
        model = request.form.get('model')
        year = request.form.get('year')
        license_plate = request.form.get('license_plate')
        service_type_id = request.form.get('service_type_id')
        requested_date = request.form.get('requested_date')
        notes = request.form.get('notes', '')
        
        # Create vehicle
        vehicle = ServiceRequestService.create_vehicle(
            type=vehicle_type,
            make=make,
            model=model,
            year=year,
            license_plate=license_plate
        )
        
        # Create service request
        service_request = ServiceRequestService.create_service_request(
            user_id=current_user.id,
            vehicle_id=vehicle.id,
            service_type_id=service_type_id,
            requested_date=datetime.strptime(requested_date, '%Y-%m-%d'),
            notes=notes
        )
        
        flash('Service request created successfully', 'success')
        return redirect(url_for('user.dashboard'))
    
    return render_template('user/book_service.html', service_types=service_types)

@user.route('/user/service-requests')
@login_required
def service_requests():
    """User service requests route"""
    if current_user.role != 'user':
        return redirect(url_for('main.dashboard'))
    
    service_requests = ServiceRequestService.get_user_requests(current_user.id)
    return render_template('user/service_requests.html', service_requests=service_requests)

@user.route('/user/delete-request/<int:request_id>', methods=['POST'])
@login_required
def delete_request(request_id):
    """User deletes own completed service request"""
    # Fetch the request
    req = ServiceRequestService.get_user_requests(current_user.id)
    # Delete only if belongs to user and status completed
    request_obj = ServiceRequestService.delete_request(request_id)  # using service delete_request
    # Actually, fetch and check status
    from app.infrastructure.persistence.models.db_models import ServiceRequest
    req_obj = ServiceRequest.query.get(request_id)
    if not req_obj or req_obj.user_id != current_user.id:
        flash('Service request not found or unauthorized', 'danger')
    elif req_obj.status != 'completed':
        flash('Only completed requests can be deleted', 'danger')
    else:
        success, message = ServiceRequestService.delete_request(request_id)
        flash(message, 'success' if success else 'danger')
    return redirect(url_for('user.service_requests')) 