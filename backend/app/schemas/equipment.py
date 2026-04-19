from datetime import datetime
from pydantic import BaseModel, Field


class EquipmentCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    category: str = Field(..., min_length=1, max_length=100)
    brand: str = ""
    model: str = ""
    cooling_capacity: float = 0.0
    heating_capacity: float = 0.0
    rated_cop: float = 0.0
    rated_power: float = 0.0
    performance_curves: dict = {}
    price: float = 0.0
    specs: dict = {}


class EquipmentUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    brand: str | None = None
    model: str | None = None
    cooling_capacity: float | None = None
    heating_capacity: float | None = None
    rated_cop: float | None = None
    rated_power: float | None = None
    performance_curves: dict | None = None
    price: float | None = None
    specs: dict | None = None


class EquipmentResponse(BaseModel):
    id: str
    name: str
    category: str
    brand: str
    model: str
    cooling_capacity: float
    heating_capacity: float
    rated_cop: float
    rated_power: float
    performance_curves: dict
    price: float
    specs: dict
    created_at: datetime

    model_config = {"from_attributes": True}
