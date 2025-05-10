"""
Dependency injection container to wire up repositories and use cases.
This is the glue between the domain, application, and infrastructure layers.
"""
from app.domain.repositories.user_repository import UserRepository
from app.domain.repositories.service_request_repository import ServiceRequestRepository

from app.infrastructure.persistence.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository

from app.application.use_cases.user_authentication import UserAuthenticationUseCase

class DIContainer:
    """
    Simple dependency injection container to wire up the application.
    """
    
    def __init__(self):
        self._repositories = {}
        self._use_cases = {}
        self._initialize()
    
    def _initialize(self):
        # Initialize repositories
        self._repositories[UserRepository] = SQLAlchemyUserRepository()
        
        # Initialize use cases
        self._use_cases[UserAuthenticationUseCase] = UserAuthenticationUseCase(
            user_repository=self._repositories[UserRepository]
        )
    
    def get_repository(self, repository_class):
        """Get a repository instance"""
        return self._repositories[repository_class]
    
    def get_use_case(self, use_case_class):
        """Get a use case instance"""
        return self._use_cases[use_case_class]

# Create a global container instance
container = DIContainer() 