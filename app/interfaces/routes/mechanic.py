from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.infrastructure.persistence.models.db_models import ServiceRequest
from app.application.services.service_request_service import ServiceRequestService

mechanic = Blueprint('mechanic', __name__)

@mechanic.route('/mechanic/dashboard')
@login_required
def dashboard():
    """Mechanic dashboard route"""
    if current_user.role != 'mechanic':
        return redirect(url_for('main.dashboard'))
    
    # Get pending requests and mechanic's assigned requests
    pending_requests = ServiceRequestService.get_pending_requests()
    mechanic_requests = ServiceRequestService.get_mechanic_requests(current_user.id)
    
    return render_template('mechanic/dashboard.html', 
                           pending_requests=pending_requests,
                           mechanic_requests=mechanic_requests)

@mechanic.route('/mechanic/accept-request/<int:request_id>')
@login_required
def accept_request(request_id):
    """Accept service request route"""
    if current_user.role != 'mechanic':
        return redirect(url_for('main.dashboard'))
    
    success, message = ServiceRequestService.update_request_status(
        request_id=request_id,
        status='accepted',
        mechanic_id=current_user.id
    )
    
    if success:
        flash(message, 'success')
    else:
        flash(message, 'danger')
    
    return redirect(url_for('mechanic.dashboard'))

@mechanic.route('/mechanic/reject-request/<int:request_id>')
@login_required
def reject_request(request_id):
    """Reject service request route"""
    if current_user.role != 'mechanic':
        return redirect(url_for('main.dashboard'))
    
    success, message = ServiceRequestService.update_request_status(
        request_id=request_id,
        status='rejected'
    )
    
    if success:
        flash(message, 'success')
    else:
        flash(message, 'danger')
    
    return redirect(url_for('mechanic.dashboard'))

@mechanic.route('/mechanic/update-status/<int:request_id>', methods=['POST'])
@login_required
def update_status(request_id):
    """Update service status route"""
    if current_user.role != 'mechanic':
        return redirect(url_for('main.dashboard'))
    
    status = request.form.get('status')
    
    success, message = ServiceRequestService.update_request_status(
        request_id=request_id,
        status=status
    )
    
    if success:
        flash(message, 'success')
    else:
        flash(message, 'danger')
    
    return redirect(url_for('mechanic.dashboard'))

@mechanic.route('/mechanic/delete-request/<int:request_id>', methods=['POST'])
@login_required
def delete_request(request_id):
    """Mechanic deletes a completed service request"""
    if current_user.role != 'mechanic':
        return redirect(url_for('main.dashboard'))

    success, message = ServiceRequestService.delete_request(request_id)
    if success:
        flash(message, 'success')
    else:
        flash(message, 'danger')
    
    return redirect(url_for('mechanic.dashboard')) 