from typing import Optional
from werkzeug.security import check_password_hash

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository


class UserAuthenticationUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def authenticate(self, username: str, password: str) -> Optional[User]:
        """
        Authenticate a user with username and password
        
        Args:
            username: The username to authenticate
            password: The password to authenticate
            
        Returns:
            User entity if authenticated, None otherwise
        """
        user = self.user_repository.find_by_username(username)
        
        if not user:
            return None
        
        # Check if password matches
        if not check_password_hash(user.password, password):
            return None
            
        return user
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Get a user by ID
        
        Args:
            user_id: The user ID to lookup
            
        Returns:
            User entity if found, None otherwise
        """
        return self.user_repository.find_by_id(user_id) 