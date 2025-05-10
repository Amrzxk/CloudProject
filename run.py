from app import create_app, db
from app.infrastructure.persistence.models.db_models import User, ServiceType
from werkzeug.security import generate_password_hash

app = create_app()

# Create a function to seed data
def create_seed_data():
    # Ensure all desired service types exist in database
    desired = [
        ('Oil Change', 'Regular oil change service'),
        ('Tire Rotation', 'Rotate tires for even wear'),
        ('Brake Service', 'Inspect and service brake system'),
        ('Engine Tune-up', 'Tune up engine for optimal performance'),
        ('Bike Service', 'General bike maintenance'),
        ('Battery Replacement', 'Replace and test vehicle battery'),
        ('Wheel Alignment', 'Align wheels for better handling'),
        ('Air Filter Replacement', 'Replace air filters for engine protection'),
        ('Transmission Service', 'Inspect and service transmission'),
        ('Coolant Flush', 'Flush and replace engine coolant'),
        ('Full Inspection', 'Comprehensive vehicle inspection')
    ]
    for name, desc in desired:
        if not ServiceType.query.filter_by(name=name).first():
            db.session.add(ServiceType(name=name, description=desc))
    db.session.commit()
    # Seed sample users if none exist
    if User.query.count() == 0:
        
        # Create sample users (mechanic and regular user)
        mechanic = User(
            username='mechanic',
            email='mechanic@example.com',
            password=generate_password_hash('password'),
            role='mechanic'
        )
        
        user = User(
            username='user',
            email='user@example.com',
            password=generate_password_hash('password'),
            role='user'
        )
        
        db.session.add(mechanic)
        db.session.add(user)
        db.session.commit()

# For Flask 2.0+, we need to use with app.app_context() instead of before_first_request
with app.app_context():
    create_seed_data()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 