from typing import Dict
from typing import List
from typing import Optional

from pydantic import BaseModel


class HealthComponent(BaseModel):
    component_type: str
    metric_value: str
    metric_unit: str
    status: str
    timestamp: float


class HealthResponse(BaseModel):
    status: str
    description: Optional[str]
    version: Optional[str]
    details: Optional[Dict[str, List[HealthComponent]]]