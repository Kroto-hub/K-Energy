export interface Project {
  id: string;
  name: string;
  description?: string;
  location: string;
  status: string;
  created_at?: string;
  updated_at?: string;
  buildingArea?: number;
  province?: string;
  city_name?: string;
  weather_city_id?: string;
  default_epw_file_id?: string;
  design_mode?: string;
  weather_file?: string;
}

export interface ProjectBuilding {
  id: string;
  project_id: string;
  name: string;
  building_type: string;
  climate_zone: string;
  room_usage: string;
  cooling_load_coeff: number;
  heating_load_coeff: number;
  electric_load_coeff: number;
  building_count: number;
  building_height: number;
  floors: number;
  area: number;
  floor_area: number;
  shape_coeff: number;
  orientation_angle: number;
  roof_type: string;
  roof_u: number;
  wall_u: number;
  floor_u: number;
  window_u: number;
  window_shgc: number;
  wwr_south: number;
  wwr_north: number;
  wwr_east: number;
  wwr_west: number;
  winter_temp: number;
  winter_humidity: number;
  summer_temp: number;
  summer_humidity: number;
  cooling_start_month: number;
  cooling_start_day: number;
  cooling_end_month: number;
  cooling_end_day: number;
  heating_start_month: number;
  heating_start_day: number;
  heating_end_month: number;
  heating_end_day: number;
  occupancy_density: number;
  lighting_density: number;
  equipment_density: number;
  fresh_air_rate: number;
  labor_intensity: string;
  infiltration_rate: number;
  default_usage_template_id: string;
  default_schedule_group_id: string;
  default_people_schedule_id: string;
  default_lighting_schedule_id: string;
  default_equipment_schedule_id: string;
  default_hvac_schedule_id: string;
  default_fresh_air_schedule_id: string;
  default_roof_template_id: string;
  default_wall_template_id: string;
  default_window_template_id: string;
  default_floor_template_id: string;
  default_construction_template_id: string;
  floors_data: BuildingFloorData[];
  created_at: string;
}

export interface BuildingFloorData {
  floor_index: number;
  floor_name: string;
  usage_type: string;
  area: number;
  height: number;
  inherit_default: boolean;
  overrides?: {
    occupancy_density?: number;
    lighting_density?: number;
    equipment_density?: number;
    fresh_air_rate?: number;
    infiltration_rate?: number;
    summer_temp?: number;
    winter_temp?: number;
    floor_u?: number;
    wall_u?: number;
    window_u?: number;
    window_shgc?: number;
    wwr_south?: number;
    wwr_north?: number;
    wwr_east?: number;
    wwr_west?: number;
  };
}

export interface SimulationResultSummary {
  hourly_cooling: number[];
  hourly_heating: number[];
  total_cooling_kwh: number;
  total_heating_kwh: number;
  max_cooling_kw: number;
  max_heating_kw: number;
}

export interface SimulationJob {
  id: string;
  project_id: string;
  building_id?: string | null;
  scheme_id?: string | null;
  job_type: string;
  load_source_type: string;
  status: string;
  progress: number;
  started_at?: string | null;
  finished_at?: string | null;
  output_dir?: string;
  error_message?: string;
  triggered_by?: string;
  created_at: string;
  result_summary?: SimulationResultSummary | null;
}

export interface ProjectBuildingLoadSummary {
  building_id: string;
  building_name: string;
  building_type: string;
  floors: number;
  area: number;
  latest_job?: SimulationJob | null;
  result_summary?: SimulationResultSummary | null;
}

export interface ProjectLoadSummary {
  project_id: string;
  project_name: string;
  building_count: number;
  completed_building_count: number;
  total_cooling_kwh: number;
  total_heating_kwh: number;
  max_cooling_kw: number;
  max_heating_kw: number;
  hourly_cooling: number[];
  hourly_heating: number[];
  buildings: ProjectBuildingLoadSummary[];
}

export interface Equipment {
  id: string;
  name: string;
  type: string;
  brand: string;
  capacity: number;
  unit: string;
}

export interface EnergyStation {
  id: string;
  project_id: string;
  name: string;
  description?: string;
  chillers: Array<{
    id: string;
    name: string;
    count: number;
    cooling_capacity: number;
    heating_capacity: number;
    rated_power: number;
    rated_cop: number;
    purchase_price: number;
  }>;
  heat_pumps: Array<Record<string, any>>;
  storage_units: Array<{
    id: string;
    name: string;
    count: number;
    rated_capacity_kwh: number;
    max_charge_power_kw: number;
    max_discharge_power_kw: number;
    purchase_price: number;
  }>;
  installation_rate: number;
  pipe_rate: number;
  electrical_rate: number;
  other_rate: number;
  electricity_price: number;
  gas_price: number;
  water_price: number;
  maintenance_rate: number;
  peak_electricity_price: number;
  flat_electricity_price: number;
  valley_electricity_price: number;
  created_at?: string;
  updated_at?: string;
}

export interface CalculationResult {
  initialCost: number;
  annualOperationCost: number;
  hourlyLoads?: number[];
  hourlyCOP?: number[];
}
