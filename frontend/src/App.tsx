import { Routes, Route, Navigate } from "react-router-dom";
import AppLayout from "./components/Layout/AppLayout";
import ProjectList from "./pages/ProjectList";
import ProjectDetail from "./pages/ProjectDetail";
import EnergyStationConfig from "./pages/EnergyStationConfig";
import EquipmentManage from "./pages/EquipmentManage";
import LoadAnalysis from "./pages/LoadAnalysis";
import CostCalculation from "./pages/CostCalculation";
import ReportExport from "./pages/ReportExport";

const App: React.FC = () => {
  return (
    <Routes>
      <Route path="/" element={<AppLayout />}>
        <Route index element={<Navigate to="/projects" replace />} />
        <Route path="projects" element={<ProjectList />} />
        <Route path="projects/:id" element={<ProjectDetail />} />
        <Route path="projects/:id/station" element={<EnergyStationConfig />} />
        <Route path="equipment" element={<EquipmentManage />} />
        <Route path="projects/:id/load" element={<LoadAnalysis />} />
        <Route path="projects/:id/cost" element={<CostCalculation />} />
        <Route path="projects/:id/report" element={<ReportExport />} />
      </Route>
    </Routes>
  );
};

export default App;
