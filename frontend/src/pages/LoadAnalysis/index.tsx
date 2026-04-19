import { Card, Empty } from "antd";

const LoadAnalysis: React.FC = () => {
  return (
    <Card title="负荷分析（8760小时）">
      <Empty description="请先完成能源站配置并运行 EnergyPlus 模拟" />
    </Card>
  );
};

export default LoadAnalysis;
