import { Routes, Route, Navigate } from "react-router-dom";
import AppLayout from "./components/Layout/AppLayout";
import ProjectList from "./pages/ProjectList";
import WeatherConfig from "./pages/WeatherConfig";
import BuildingList from "./pages/BuildingList";
import BuildingConfig from "./pages/BuildingConfig";
import BuildingFloors from "./pages/BuildingFloors";
import EnvelopeConfig from "./pages/EnvelopeConfig";
import ConstructionTemplateManage from "./pages/ConstructionTemplateManage";
import ScheduleTemplateManage from "./pages/ScheduleTemplateManage";
import EnergyStationConfig from "./pages/EnergyStationConfig";
import EquipmentManage from "./pages/EquipmentManage";
import LoadAnalysis from "./pages/LoadAnalysis";
import ProjectLoadSummaryPage from "./pages/ProjectLoadSummary";
import SchemeComparePage from "./pages/SchemeCompare";
import CostCalculation from "./pages/CostCalculation";
import ReportExport from "./pages/ReportExport";

// Placeholders for new pages
const OperationTimePlaceholder = () => <div style={{ padding: 24 }}>运行时间配置 (待开发)</div>;

const App: React.FC = () => {
  return (
    <Routes>
      <Route path="/" element={<AppLayout />}>
        <Route index element={<Navigate to="/projects" replace />} />
        <Route path="projects" element={<ProjectList />} />
        
        <Route path="projects/:id">
          <Route index element={<Navigate to="buildings" replace />} />
          <Route path="weather" element={<WeatherConfig />} />
          <Route path="buildings" element={<BuildingList />} />
          <Route path="buildings/:buildingId/model" element={<BuildingConfig />} />
          <Route path="buildings/:buildingId/floors" element={<BuildingFloors />} />
          <Route path="buildings/:buildingId/envelope" element={<EnvelopeConfig />} />
          <Route path="buildings/:buildingId/load" element={<LoadAnalysis />} />
          <Route path="building" element={<BuildingConfig />} />
          <Route path="construction-templates" element={<ConstructionTemplateManage />} />
          <Route path="schedules" element={<ScheduleTemplateManage />} />
          <Route path="operation" element={<OperationTimePlaceholder />} />
          <Route path="station" element={<EnergyStationConfig />} />
          <Route path="schemes" element={<SchemeComparePage />} />
          <Route path="load" element={<ProjectLoadSummaryPage />} />
          <Route path="cost" element={<CostCalculation />} />
          <Route path="report" element={<ReportExport />} />
        </Route>
        
        <Route path="database" element={<EquipmentManage />} />
      </Route>
    </Routes>
  );
};

export default App;
