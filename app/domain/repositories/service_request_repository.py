from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

from app.domain.entities.service_request import ServiceRequest


class ServiceRequestRepository(ABC):
    @abstractmethod
    def find_by_id(self, request_id: int) -> Optional[ServiceRequest]:
        pass
    
    @abstractmethod
    def find_by_user_id(self, user_id: int) -> List[ServiceRequest]:
        pass
    
    @abstractmethod
    def find_by_mechanic_id(self, mechanic_id: int) -> List[ServiceRequest]:
        pass
    
    @abstractmethod
    def find_by_status(self, status: str) -> List[ServiceRequest]:
        pass
    
    @abstractmethod
    def find_by_date_range(self, start_date: datetime, end_date: datetime) -> List[ServiceRequest]:
        pass
    
    @abstractmethod
    def find_all(self) -> List[ServiceRequest]:
        pass
    
    @abstractmethod
    def save(self, service_request: ServiceRequest) -> ServiceRequest:
        pass
    
    @abstractmethod
    def delete(self, request_id: int) -> bool:
        pass 