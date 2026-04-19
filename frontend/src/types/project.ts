export interface Project {
  id: string;
  name: string;
  location: string;
  status: string;
  createdAt: string;
  buildingArea?: number;
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
  projectId: string;
  name: string;
  chillerType?: string;
  coolingCapacity?: number;
  ratedCOP?: number;
  heatingType?: string;
  heatingCapacity?: number;
}

export interface CalculationResult {
  initialCost: number;
  annualOperationCost: number;
  hourlyLoads?: number[];
  hourlyCOP?: number[];
}
