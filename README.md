# Vehicle Service Booking System

A web application that allows users to book vehicle service appointments and mechanics to manage service requests. Built using Flask and SQLAlchemy with a focus on clean architecture principles.

## Features

- **User Authentication**
  - User account creation and login
  - Role-based access control (user, mechanic)
  - Secure password hashing
  
- **Vehicle Management**
  - Add car or bike details
  - Store vehicle specifications
  - Associate vehicles with service requests
  
- **Service Booking**
  - Book service appointments with preferred date
  - Multiple service types support
  - Add service notes and requirements
  
- **Mechanic Dashboard**
  - View and manage pending service requests
  - Accept/reject service appointments
  - Update service status
  
- **Service Tracking**
  - Track service request progress
  - View service history
  - Status updates (pending, accepted, in progress, completed, rejected)

## Technology Stack

- **Backend**
  - Python 3.9
  - Flask Web Framework
  - SQLAlchemy ORM
  - Flask-Login for authentication
  
- **Database**
  - SQLite (development)
  - Compatible with PostgreSQL (production)
  
- **Frontend**
  - HTML/CSS
  - Bootstrap for responsive design
  
- **Containerization**
  - Docker
  - Docker Compose

## Clean Architecture

The project strictly follows clean architecture principles to ensure maintainability, testability, and separation of concerns:

### 1. Domain Layer (`app/domain/`)
- **Entities**: Pure Python dataclasses representing business objects (User, Vehicle, ServiceRequest, ServiceType)
- **Repositories**: Abstract interfaces defining data access methods
- **Independent**: Contains no dependencies on frameworks or external libraries

### 2. Application Layer (`app/application/`)
- **Use Cases**: Implements business logic 
- **Services**: Implements application-specific logic
- **Depends only on**: Domain layer

### 3. Interface Layer (`app/interfaces/`)
- **Routes**: Flask blueprints for HTTP routing
- **Templates**: HTML templates for views
- **Static assets**: CSS, JavaScript, and images
- **Depends on**: Application layer

### 4. Infrastructure Layer (`app/infrastructure/`)
- **Persistence**: Database models and repository implementations
- **Web**: Flask-specific code
- **External services**: Integration with external APIs
- **Depends on**: Domain and Application layers

## Project Structure

```
app/
├── __init__.py                 # Flask application factory
├── domain/                     # Domain layer (business rules)
│   ├── entities/               # Business entities (pure Python)
│   │   ├── user.py
│   │   ├── vehicle.py
│   │   ├── service_request.py
│   │   └── service_type.py
│   └── repositories/           # Repository interfaces
│       ├── user_repository.py
│       └── service_request_repository.py
├── application/                # Application layer
│   ├── services/               # Application services
│   │   ├── auth_service.py
│   │   └── service_request_service.py
│   └── use_cases/              # Business use cases
│       └── user_authentication.py
├── interfaces/                 # Interface layer
│   ├── routes/                 # Flask routes
│   │   ├── auth.py
│   │   ├── main.py
│   │   ├── mechanic.py
│   │   └── user.py
│   ├── templates/              # Jinja2 templates
│   └── static/                 # Static assets
└── infrastructure/             # Infrastructure layer
    ├── persistence/            # Database implementation
    │   ├── models/             # SQLAlchemy models
    │   │   └── db_models.py
    │   └── repositories/       # Repository implementations
    │       └── sqlalchemy_user_repository.py
    └── di_container.py         # Dependency injection container
```

## Setup Instructions

### Local Development

1. Clone the repository:
   ```
   git clone <repository-url>
   cd vehicle-service-booking
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python run.py
   ```

5. Visit http://localhost:5000 in your browser

### Docker Setup

#### Using Docker Compose (Recommended)

1. Make sure you have Docker and Docker Compose installed on your system.

2. Build and run the application using Docker Compose:
   ```
   docker-compose up --build
   ```

3. Visit http://localhost:5000 in your browser

4. To stop the application:
   ```
   docker-compose down
   ```

#### Using Docker Directly

1. Build the Docker image:
   ```
   docker build -t vehicle-service-booking .
   ```

2. Run the container:
   ```
   docker run -p 5000:5000 vehicle-service-booking
   ```

3. Visit http://localhost:5000 in your browser

## Environment Variables

You can customize the application behavior using environment variables:

| Variable         | Description                       | Default Value        |
|------------------|-----------------------------------|----------------------|
| SECRET_KEY       | Flask secret key                  | dev-key-for-testing  |
| DATABASE_URL     | Database connection URI           | sqlite:///vehicleservice.db |
| FLASK_ENV        | Flask environment (development/production) | production |

## Cloud Deployment

### Heroku Deployment

1. Login to Heroku CLI:
   ```
   heroku login
   ```

2. Create a Heroku app:
   ```
   heroku create vehicle-service-booking
   ```

3. Push to Heroku:
   ```
   git push heroku main
   ```

### AWS Deployment

1. Create an ECR repository
   ```
   aws ecr create-repository --repository-name vehicle-service-booking
   ```

2. Build and tag the Docker image
   ```
   docker build -t <aws-account-id>.dkr.ecr.<region>.amazonaws.com/vehicle-service-booking:latest .
   ```

3. Push the image to ECR
   ```
   aws ecr get-login-password | docker login --username AWS --password-stdin <aws-account-id>.dkr.ecr.<region>.amazonaws.com
   docker push <aws-account-id>.dkr.ecr.<region>.amazonaws.com/vehicle-service-booking:latest
   ```

4. Deploy using ECS or EKS

## Default Users

For testing purposes, the system comes with pre-created accounts:

- Regular User:
  - Username: `user`
  - Password: `password`

- Mechanic:
  - Username: `mechanic`
  - Password: `password`

## Development

### Adding New Models

1. Create a new entity in `app/domain/entities/`
2. Define repository interface in `app/domain/repositories/` 
3. Add SQLAlchemy model in `app/infrastructure/persistence/models/db_models.py`
4. Implement repository in `app/infrastructure/persistence/repositories/`
5. Register in dependency injection container

### Running Tests

```
python -m pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 