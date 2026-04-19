from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ENERGYPLUS_DIR = BASE_DIR / "EnergyPlus"
ENERGYPLUS_EXE = ENERGYPLUS_DIR / "energyplus.exe"
ENERGYPLUS_WEATHER_DIR = ENERGYPLUS_DIR / "WeatherData"

DATA_DIR = BASE_DIR / "data"
WEATHER_DIR = DATA_DIR / "weather"
EQUIPMENT_DB_DIR = DATA_DIR / "equipment_db"
TEMPLATES_DIR = DATA_DIR / "templates"

DATABASE_URL = f"sqlite:///{BASE_DIR / 'data' / 'k_energy.db'}"

CORS_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
