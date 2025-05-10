from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ServiceType:
    name: str
    description: Optional[str] = None
    id: Optional[int] = None
    service_requests: List['ServiceRequest'] = field(default_factory=list)
    
    def __repr__(self):
        return f'<ServiceType {self.name}>' 