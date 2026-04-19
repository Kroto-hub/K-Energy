from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.project import Project, EnergyStation, Equipment
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from app.schemas.energy_station import EnergyStationCreate, EnergyStationUpdate, EnergyStationResponse
from app.schemas.equipment import EquipmentCreate, EquipmentUpdate, EquipmentResponse

router = APIRouter()


@router.get("/projects", response_model=List[ProjectResponse])
def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).order_by(Project.created_at.desc()).all()


@router.post("/projects", response_model=ProjectResponse, status_code=201)
def create_project(data: ProjectCreate, db: Session = Depends(get_db)):
    project = Project(**data.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.get("/projects/{project_id}", response_model=ProjectResponse)
def get_project(project_id: str, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="项目不存在")
    return project


@router.put("/projects/{project_id}", response_model=ProjectResponse)
def update_project(project_id: str, data: ProjectUpdate, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="项目不存在")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(project, key, value)
    db.commit()
    db.refresh(project)
    return project


@router.delete("/projects/{project_id}")
def delete_project(project_id: str, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="项目不存在")
    db.delete(project)
    db.commit()
    return {"message": "删除成功"}


@router.get("/projects/{project_id}/stations", response_model=List[EnergyStationResponse])
def list_stations(project_id: str, db: Session = Depends(get_db)):
    return db.query(EnergyStation).filter(EnergyStation.project_id == project_id).all()


@router.post("/projects/{project_id}/stations", response_model=EnergyStationResponse, status_code=201)
def create_station(project_id: str, data: EnergyStationCreate, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="项目不存在")
    station = EnergyStation(project_id=project_id, **data.model_dump(exclude={"project_id"}))
    db.add(station)
    db.commit()
    db.refresh(station)
    return station


@router.put("/stations/{station_id}", response_model=EnergyStationResponse)
def update_station(station_id: str, data: EnergyStationUpdate, db: Session = Depends(get_db)):
    station = db.query(EnergyStation).filter(EnergyStation.id == station_id).first()
    if not station:
        raise HTTPException(status_code=404, detail="能源站不存在")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(station, key, value)
    db.commit()
    db.refresh(station)
    return station


@router.get("/equipment", response_model=List[EquipmentResponse])
def list_equipment(category: str = None, db: Session = Depends(get_db)):
    query = db.query(Equipment)
    if category:
        query = query.filter(Equipment.category == category)
    return query.order_by(Equipment.created_at.desc()).all()


@router.post("/equipment", response_model=EquipmentResponse, status_code=201)
def create_equipment(data: EquipmentCreate, db: Session = Depends(get_db)):
    equipment = Equipment(**data.model_dump())
    db.add(equipment)
    db.commit()
    db.refresh(equipment)
    return equipment


@router.put("/equipment/{equipment_id}", response_model=EquipmentResponse)
def update_equipment(equipment_id: str, data: EquipmentUpdate, db: Session = Depends(get_db)):
    equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=404, detail="设备不存在")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(equipment, key, value)
    db.commit()
    db.refresh(equipment)
    return equipment


@router.delete("/equipment/{equipment_id}")
def delete_equipment(equipment_id: str, db: Session = Depends(get_db)):
    equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=404, detail="设备不存在")
    db.delete(equipment)
    db.commit()
    return {"message": "删除成功"}
