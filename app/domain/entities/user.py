from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class User:
    username: str
    email: str
    password: str  # This would be the hashed password
    role: str = "user"  # 'user' or 'mechanic'
    created_at: datetime = field(default_factory=datetime.utcnow)
    id: Optional[int] = None
    service_requests: List['ServiceRequest'] = field(default_factory=list)
    assigned_service_requests: List['ServiceRequest'] = field(default_factory=list)

    def __repr__(self):
        return f'<User {self.username}>' 