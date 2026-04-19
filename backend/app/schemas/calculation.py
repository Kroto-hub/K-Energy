from datetime import datetime
from pydantic import BaseModel


class CalculationResultResponse(BaseModel):
    id: str
    project_id: str
    station_id: str
    equipment_cost: float
    installation_cost: float
    pipe_cost: float
    electrical_cost: float
    other_cost: float
    total_initial_cost: float
    annual_electricity_cost: float
    annual_gas_cost: float
    annual_water_cost: float
    annual_maintenance_cost: float
    total_annual_cost: float
    annual_electricity_consumption: float
    annual_gas_consumption: float
    details: dict
    created_at: datetime

    model_config = {"from_attributes": True}
