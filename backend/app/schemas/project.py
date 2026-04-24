from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator

class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    location: Optional[str] = ""
    building_area: Optional[float] = 0.0
    description: Optional[str] = ""
    weather_file: Optional[str] = ""
    province: Optional[str] = ""
    city_name: Optional[str] = ""
    weather_city_id: Optional[str] = ""
    default_epw_file_id: Optional[str] = ""
    design_mode: Optional[str] = "估算"

    @field_validator('building_area', mode='before')
    def parse_building_area(cls, v):
        if v == "" or v is None:
            return 0.0
        return v


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    building_area: Optional[float] = None
    description: Optional[str] = None
    status: Optional[str] = None
    weather_file: Optional[str] = None
    province: Optional[str] = None
    city_name: Optional[str] = None
    weather_city_id: Optional[str] = None
    default_epw_file_id: Optional[str] = None
    design_mode: Optional[str] = None


class ProjectResponse(BaseModel):
    id: str
    name: str
    location: str
    building_area: float
    description: str
    status: str
    weather_file: str
    province: str
    city_name: str
    weather_city_id: str
    default_epw_file_id: str
    design_mode: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

class ProjectBuildingBase(BaseModel):
    name: str = "Main Building"
    building_type: str = "办公建筑"
    climate_zone: str = "寒冷地区"
    room_usage: str = ""
    
    cooling_load_coeff: float = 1.0
    heating_load_coeff: float = 1.0
    electric_load_coeff: float = 1.0
    building_count: int = 1
    
    building_height: float = 48.0
    floors: int = 12
    area: float = 25920.0
    floor_area: float = 2160.0
    shape_coeff: float = 0.12
    orientation_angle: float = 0.0
    roof_type: str = "平屋顶"
    
    roof_u: float = 0.35
    wall_u: float = 0.45
    floor_u: float = 0.5
    window_u: float = 2.3
    window_shgc: float = 0.4
    wwr_south: float = 0.4
    wwr_north: float = 0.4
    wwr_east: float = 0.3
    wwr_west: float = 0.3
    
    winter_temp: float = 20.0
    winter_humidity: float = 50.0
    summer_temp: float = 26.0
    summer_humidity: float = 60.0
    cooling_start_month: int = Field(default=6, ge=1, le=12)
    cooling_start_day: int = Field(default=1, ge=1, le=31)
    cooling_end_month: int = Field(default=9, ge=1, le=12)
    cooling_end_day: int = Field(default=30, ge=1, le=31)
    heating_start_month: int = Field(default=11, ge=1, le=12)
    heating_start_day: int = Field(default=15, ge=1, le=31)
    heating_end_month: int = Field(default=3, ge=1, le=12)
    heating_end_day: int = Field(default=15, ge=1, le=31)
    
    occupancy_density: float = 0.1
    lighting_density: float = 9.0
    equipment_density: float = 15.0
    fresh_air_rate: float = 30.0
    labor_intensity: str = "静坐"
    infiltration_rate: float = 1.0

    default_usage_template_id: str = ""
    default_schedule_group_id: str = ""
    default_people_schedule_id: str = ""
    default_lighting_schedule_id: str = ""
    default_equipment_schedule_id: str = ""
    default_hvac_schedule_id: str = ""
    default_fresh_air_schedule_id: str = ""
    default_roof_template_id: str = ""
    default_wall_template_id: str = ""
    default_window_template_id: str = ""
    default_floor_template_id: str = ""
    default_construction_template_id: str = ""

    floors_data: list = []

class ProjectBuildingCreate(ProjectBuildingBase):
    pass

class ProjectBuildingResponse(ProjectBuildingBase):
    id: str
    project_id: str
    created_at: datetime
    
    model_config = {"from_attributes": True}
