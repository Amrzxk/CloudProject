from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class ServiceRequest:
    user_id: int
    vehicle_id: int
    service_type_id: int
    requested_date: datetime
    mechanic_id: Optional[int] = None
    status: str = "pending"  # 'pending', 'accepted', 'in_progress', 'completed', 'rejected'
    notes: Optional[str] = None
    id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    
    def __repr__(self):
        return f'<ServiceRequest {self.id} - {self.status}>' 