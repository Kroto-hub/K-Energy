import uuid
from datetime import datetime
from sqlalchemy import String, Float, Integer, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.models.common import generate_uuid


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    location: Mapped[str] = mapped_column(String(200), default="")
    building_area: Mapped[float] = mapped_column(Float, default=0.0)
    description: Mapped[str] = mapped_column(Text, default="")
    status: Mapped[str] = mapped_column(String(50), default="进行中")
    weather_file: Mapped[str] = mapped_column(String(500), default="")
    
    province: Mapped[str] = mapped_column(String(100), default="")
    city_name: Mapped[str] = mapped_column(String(100), default="")
    weather_city_id: Mapped[str] = mapped_column(String(36), default="")
    default_epw_file_id: Mapped[str] = mapped_column(String(36), default="")
    design_mode: Mapped[str] = mapped_column(String(50), default="估算")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    energy_stations = relationship("EnergyStation", back_populates="project", cascade="all, delete-orphan")
    calculation_results = relationship("CalculationResult", back_populates="project", cascade="all, delete-orphan")


class ProjectBuilding(Base):
    __tablename__ = "project_buildings"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    project_id: Mapped[str] = mapped_column(String(36), ForeignKey("projects.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(200), default="Main Building")
    building_type: Mapped[str] = mapped_column(String(100), default="办公建筑")
    climate_zone: Mapped[str] = mapped_column(String(100), default="寒冷地区")
    room_usage: Mapped[str] = mapped_column(String(100), default="")
    
    cooling_load_coeff: Mapped[float] = mapped_column(Float, default=1.0)
    heating_load_coeff: Mapped[float] = mapped_column(Float, default=1.0)
    electric_load_coeff: Mapped[float] = mapped_column(Float, default=1.0)
    building_count: Mapped[int] = mapped_column(Integer, default=1)
    
    building_height: Mapped[float] = mapped_column(Float, default=48.0)
    floors: Mapped[int] = mapped_column(Integer, default=12)
    area: Mapped[float] = mapped_column(Float, default=25920.0)
    floor_area: Mapped[float] = mapped_column(Float, default=2160.0)
    shape_coeff: Mapped[float] = mapped_column(Float, default=0.12)
    orientation_angle: Mapped[float] = mapped_column(Float, default=0.0)
    roof_type: Mapped[str] = mapped_column(String(50), default="平屋顶")
    
    roof_u: Mapped[float] = mapped_column(Float, default=0.35)
    wall_u: Mapped[float] = mapped_column(Float, default=0.45)
    floor_u: Mapped[float] = mapped_column(Float, default=0.5)
    window_u: Mapped[float] = mapped_column(Float, default=2.3)
    window_shgc: Mapped[float] = mapped_column(Float, default=0.4)
    wwr_south: Mapped[float] = mapped_column(Float, default=0.4)
    wwr_north: Mapped[float] = mapped_column(Float, default=0.4)
    wwr_east: Mapped[float] = mapped_column(Float, default=0.3)
    wwr_west: Mapped[float] = mapped_column(Float, default=0.3)
    
    winter_temp: Mapped[float] = mapped_column(Float, default=20.0)
    winter_humidity: Mapped[float] = mapped_column(Float, default=50.0)
    summer_temp: Mapped[float] = mapped_column(Float, default=26.0)
    summer_humidity: Mapped[float] = mapped_column(Float, default=60.0)
    cooling_start_month: Mapped[int] = mapped_column(Integer, default=6)
    cooling_start_day: Mapped[int] = mapped_column(Integer, default=1)
    cooling_end_month: Mapped[int] = mapped_column(Integer, default=9)
    cooling_end_day: Mapped[int] = mapped_column(Integer, default=30)
    heating_start_month: Mapped[int] = mapped_column(Integer, default=11)
    heating_start_day: Mapped[int] = mapped_column(Integer, default=15)
    heating_end_month: Mapped[int] = mapped_column(Integer, default=3)
    heating_end_day: Mapped[int] = mapped_column(Integer, default=15)
    
    occupancy_density: Mapped[float] = mapped_column(Float, default=0.1)
    lighting_density: Mapped[float] = mapped_column(Float, default=9.0)
    equipment_density: Mapped[float] = mapped_column(Float, default=15.0)
    fresh_air_rate: Mapped[float] = mapped_column(Float, default=30.0)
    labor_intensity: Mapped[str] = mapped_column(String(50), default="静坐")
    infiltration_rate: Mapped[float] = mapped_column(Float, default=1.0)

    default_usage_template_id: Mapped[str] = mapped_column(String(36), default="")
    default_schedule_group_id: Mapped[str] = mapped_column(String(36), default="")
    default_people_schedule_id: Mapped[str] = mapped_column(String(36), default="")
    default_lighting_schedule_id: Mapped[str] = mapped_column(String(36), default="")
    default_equipment_schedule_id: Mapped[str] = mapped_column(String(36), default="")
    default_hvac_schedule_id: Mapped[str] = mapped_column(String(36), default="")
    default_fresh_air_schedule_id: Mapped[str] = mapped_column(String(36), default="")
    default_roof_template_id: Mapped[str] = mapped_column(String(36), default="")
    default_wall_template_id: Mapped[str] = mapped_column(String(36), default="")
    default_window_template_id: Mapped[str] = mapped_column(String(36), default="")
    default_floor_template_id: Mapped[str] = mapped_column(String(36), default="")
    default_construction_template_id: Mapped[str] = mapped_column(String(36), default="")
    
    floors_data: Mapped[list] = mapped_column(JSON, default=list)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    project = relationship("Project", backref="buildings")


class EnergyStation(Base):
    __tablename__ = "energy_stations"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    project_id: Mapped[str] = mapped_column(String(36), ForeignKey("projects.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, default="")

    chillers: Mapped[list] = mapped_column(JSON, default=list)
    heat_pumps: Mapped[list] = mapped_column(JSON, default=list)
    storage_units: Mapped[list] = mapped_column(JSON, default=list)
    
    chiller_type: Mapped[str] = mapped_column(String(100), default="")
    cooling_capacity: Mapped[float] = mapped_column(Float, default=0.0)
    rated_cop: Mapped[float] = mapped_column(Float, default=0.0)
    chiller_count: Mapped[int] = mapped_column(Integer, default=1)
    chiller_price: Mapped[float] = mapped_column(Float, default=0.0)

    heating_type: Mapped[str] = mapped_column(String(100), default="")
    heating_capacity: Mapped[float] = mapped_column(Float, default=0.0)
    heating_cop: Mapped[float] = mapped_column(Float, default=0.0)
    heater_count: Mapped[int] = mapped_column(Integer, default=1)
    heater_price: Mapped[float] = mapped_column(Float, default=0.0)

    pump_config: Mapped[dict] = mapped_column(JSON, default=dict)
    cooling_tower_config: Mapped[dict] = mapped_column(JSON, default=dict)
    pipe_config: Mapped[dict] = mapped_column(JSON, default=dict)

    installation_rate: Mapped[float] = mapped_column(Float, default=0.20)
    pipe_rate: Mapped[float] = mapped_column(Float, default=0.15)
    electrical_rate: Mapped[float] = mapped_column(Float, default=0.12)
    other_rate: Mapped[float] = mapped_column(Float, default=0.08)

    electricity_price: Mapped[float] = mapped_column(Float, default=0.85)
    gas_price: Mapped[float] = mapped_column(Float, default=3.5)
    water_price: Mapped[float] = mapped_column(Float, default=6.0)
    maintenance_rate: Mapped[float] = mapped_column(Float, default=0.03)

    peak_electricity_price: Mapped[float] = mapped_column(Float, default=1.2)
    flat_electricity_price: Mapped[float] = mapped_column(Float, default=0.85)
    valley_electricity_price: Mapped[float] = mapped_column(Float, default=0.4)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    project = relationship("Project", back_populates="energy_stations")


class Equipment(Base):
    __tablename__ = "equipment"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    brand: Mapped[str] = mapped_column(String(200), default="")
    model: Mapped[str] = mapped_column(String(200), default="")

    cooling_capacity: Mapped[float] = mapped_column(Float, default=0.0)
    heating_capacity: Mapped[float] = mapped_column(Float, default=0.0)
    rated_cop: Mapped[float] = mapped_column(Float, default=0.0)
    rated_power: Mapped[float] = mapped_column(Float, default=0.0)

    performance_curves: Mapped[dict] = mapped_column(JSON, default=dict)
    price: Mapped[float] = mapped_column(Float, default=0.0)

    specs: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)


class LoadProfile(Base):
    __tablename__ = "load_profiles"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    station_id: Mapped[str] = mapped_column(String(36), ForeignKey("energy_stations.id"), nullable=False)
    year: Mapped[int] = mapped_column(Integer, default=2025)
    source: Mapped[str] = mapped_column(String(100), default="energyplus")

    cooling_loads: Mapped[str] = mapped_column(Text, default="")
    heating_loads: Mapped[str] = mapped_column(Text, default="")
    electricity_loads: Mapped[str] = mapped_column(Text, default="")
    cop_values: Mapped[str] = mapped_column(Text, default="")
    outdoor_temps: Mapped[str] = mapped_column(Text, default="")

    max_cooling_load: Mapped[float] = mapped_column(Float, default=0.0)
    max_heating_load: Mapped[float] = mapped_column(Float, default=0.0)
    total_cooling_energy: Mapped[float] = mapped_column(Float, default=0.0)
    total_heating_energy: Mapped[float] = mapped_column(Float, default=0.0)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)


class CalculationResult(Base):
    __tablename__ = "calculation_results"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    project_id: Mapped[str] = mapped_column(String(36), ForeignKey("projects.id"), nullable=False)
    station_id: Mapped[str] = mapped_column(String(36), ForeignKey("energy_stations.id"), nullable=False)

    equipment_cost: Mapped[float] = mapped_column(Float, default=0.0)
    installation_cost: Mapped[float] = mapped_column(Float, default=0.0)
    pipe_cost: Mapped[float] = mapped_column(Float, default=0.0)
    electrical_cost: Mapped[float] = mapped_column(Float, default=0.0)
    other_cost: Mapped[float] = mapped_column(Float, default=0.0)
    total_initial_cost: Mapped[float] = mapped_column(Float, default=0.0)

    annual_electricity_cost: Mapped[float] = mapped_column(Float, default=0.0)
    annual_gas_cost: Mapped[float] = mapped_column(Float, default=0.0)
    annual_water_cost: Mapped[float] = mapped_column(Float, default=0.0)
    annual_maintenance_cost: Mapped[float] = mapped_column(Float, default=0.0)
    total_annual_cost: Mapped[float] = mapped_column(Float, default=0.0)

    annual_electricity_consumption: Mapped[float] = mapped_column(Float, default=0.0)
    annual_gas_consumption: Mapped[float] = mapped_column(Float, default=0.0)

    details: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    project = relationship("Project", back_populates="calculation_results")
