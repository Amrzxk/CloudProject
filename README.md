# Vehicle Service Booking System

A web application that allows users to book vehicle service appointments and mechanics to manage service requests.

## Features

- User account creation and authentication
- Booking car or bike service appointments
- Service type selection and vehicle details input
- Mechanic dashboard to view and manage service requests
- Service status updates to track progress

## Technology Stack

- Python Flask for the backend
- SQLAlchemy for database operations
- HTML/CSS for the frontend
- SQLite database (for development)
- Docker for containerization

## Project Structure

The project follows clean architecture principles with the following layers:

- **Domain Layer**: Core business entities and logic
- **Application Layer**: Application services and use cases
- **Interface Layer**: Web controllers, views and presentation
- **Infrastructure Layer**: Database, external services integration

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

1. Build the Docker image:
   ```
   docker build -t vehicle-service-booking .
   ```

2. Run the container:
   ```
   docker run -p 5000:5000 vehicle-service-booking
   ```

3. Visit http://localhost:5000 in your browser

## Cloud Deployment

The application can be deployed to various cloud platforms:

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
2. Build and tag the Docker image
3. Push the image to ECR
4. Deploy using ECS or EKS

## Default Users

For testing, the system comes with pre-created accounts:

- Regular User:
  - Username: user
  - Password: password

- Mechanic:
  - Username: mechanic
  - Password: password 