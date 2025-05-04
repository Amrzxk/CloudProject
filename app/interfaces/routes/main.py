from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Home page route"""
    return render_template('index.html')

@main.route('/dashboard')
def dashboard():
    """Dashboard page route, redirects based on user role"""
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    
    if current_user.role == 'mechanic':
        return redirect(url_for('mechanic.dashboard'))
    else:
        return redirect(url_for('user.dashboard')) 