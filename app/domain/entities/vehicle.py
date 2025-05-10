from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Vehicle:
    type: str  # 'car' or 'bike'
    make: str
    model: str
    year: int
    license_plate: str
    id: Optional[int] = None
    service_requests: List['ServiceRequest'] = field(default_factory=list)
    
    def __repr__(self):
        return f'<Vehicle {self.make} {self.model} ({self.license_plate})>' 