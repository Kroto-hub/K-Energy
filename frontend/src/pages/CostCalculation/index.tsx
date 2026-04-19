import { Card, Empty } from "antd";

const CostCalculation: React.FC = () => {
  return (
    <Card title="费用计算">
      <Empty description="请先完成负荷分析后再进行费用计算" />
    </Card>
  );
};

export default CostCalculation;
