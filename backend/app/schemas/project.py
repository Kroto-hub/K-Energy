from datetime import datetime
from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    location: str = ""
    building_area: float = 0.0
    description: str = ""
    weather_file: str = ""


class ProjectUpdate(BaseModel):
    name: str | None = None
    location: str | None = None
    building_area: float | None = None
    description: str | None = None
    status: str | None = None
    weather_file: str | None = None


class ProjectResponse(BaseModel):
    id: str
    name: str
    location: str
    building_area: float
    description: str
    status: str
    weather_file: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
