from datetime import datetime
from pydantic import BaseModel, Field


class EnergyStationCreate(BaseModel):
    project_id: str
    name: str = Field(..., min_length=1, max_length=200)
    chiller_type: str = ""
    cooling_capacity: float = 0.0
    rated_cop: float = 0.0
    chiller_count: int = 1
    chiller_price: float = 0.0
    heating_type: str = ""
    heating_capacity: float = 0.0
    heating_cop: float = 0.0
    heater_count: int = 1
    heater_price: float = 0.0
    installation_rate: float = 0.20
    pipe_rate: float = 0.15
    electrical_rate: float = 0.12
    other_rate: float = 0.08
    electricity_price: float = 0.85
    gas_price: float = 3.5
    water_price: float = 6.0
    maintenance_rate: float = 0.03
    peak_electricity_price: float = 1.2
    flat_electricity_price: float = 0.85
    valley_electricity_price: float = 0.4


class EnergyStationUpdate(BaseModel):
    name: str | None = None
    chiller_type: str | None = None
    cooling_capacity: float | None = None
    rated_cop: float | None = None
    chiller_count: int | None = None
    chiller_price: float | None = None
    heating_type: str | None = None
    heating_capacity: float | None = None
    heating_cop: float | None = None
    heater_count: int | None = None
    heater_price: float | None = None
    installation_rate: float | None = None
    pipe_rate: float | None = None
    electrical_rate: float | None = None
    other_rate: float | None = None
    electricity_price: float | None = None
    gas_price: float | None = None
    water_price: float | None = None
    maintenance_rate: float | None = None
    peak_electricity_price: float | None = None
    flat_electricity_price: float | None = None
    valley_electricity_price: float | None = None


class EnergyStationResponse(BaseModel):
    id: str
    project_id: str
    name: str
    chiller_type: str
    cooling_capacity: float
    rated_cop: float
    chiller_count: int
    chiller_price: float
    heating_type: str
    heating_capacity: float
    heating_cop: float
    heater_count: int
    heater_price: float
    installation_rate: float
    pipe_rate: float
    electrical_rate: float
    other_rate: float
    electricity_price: float
    gas_price: float
    water_price: float
    maintenance_rate: float
    peak_electricity_price: float
    flat_electricity_price: float
    valley_electricity_price: float
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
