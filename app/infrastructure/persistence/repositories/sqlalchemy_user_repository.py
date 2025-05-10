from typing import List, Optional

from app import db
from app.domain.entities.user import User as UserEntity
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.persistence.models.db_models import User as UserModel


class SQLAlchemyUserRepository(UserRepository):
    def find_by_id(self, user_id: int) -> Optional[UserEntity]:
        user_model = UserModel.query.get(user_id)
        if not user_model:
            return None
        return self._to_entity(user_model)
    
    def find_by_username(self, username: str) -> Optional[UserEntity]:
        user_model = UserModel.query.filter_by(username=username).first()
        if not user_model:
            return None
        return self._to_entity(user_model)
    
    def find_by_email(self, email: str) -> Optional[UserEntity]:
        user_model = UserModel.query.filter_by(email=email).first()
        if not user_model:
            return None
        return self._to_entity(user_model)
    
    def find_all(self) -> List[UserEntity]:
        user_models = UserModel.query.all()
        return [self._to_entity(user_model) for user_model in user_models]
    
    def find_by_role(self, role: str) -> List[UserEntity]:
        user_models = UserModel.query.filter_by(role=role).all()
        return [self._to_entity(user_model) for user_model in user_models]
    
    def save(self, user: UserEntity) -> UserEntity:
        # If user has ID, try to find existing record
        if user.id:
            user_model = UserModel.query.get(user.id)
            if user_model:
                # Update existing record
                user_model.username = user.username
                user_model.email = user.email
                user_model.password = user.password
                user_model.role = user.role
            else:
                # Not found, create new with specified ID
                user_model = UserModel(
                    id=user.id,
                    username=user.username,
                    email=user.email,
                    password=user.password,
                    role=user.role,
                    created_at=user.created_at
                )
                db.session.add(user_model)
        else:
            # Create new without ID
            user_model = UserModel(
                username=user.username,
                email=user.email,
                password=user.password,
                role=user.role,
                created_at=user.created_at
            )
            db.session.add(user_model)
        
        db.session.commit()
        return self._to_entity(user_model)
    
    def delete(self, user_id: int) -> bool:
        user_model = UserModel.query.get(user_id)
        if not user_model:
            return False
        
        db.session.delete(user_model)
        db.session.commit()
        return True
    
    def _to_entity(self, user_model: UserModel) -> UserEntity:
        """Convert ORM model to domain entity"""
        return UserEntity(
            id=user_model.id,
            username=user_model.username,
            email=user_model.email,
            password=user_model.password,
            role=user_model.role,
            created_at=user_model.created_at,
            # We're not loading related entities here to avoid circular dependencies
            service_requests=[],
            assigned_service_requests=[]
        ) 