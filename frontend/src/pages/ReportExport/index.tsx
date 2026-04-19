import { Card, Empty } from "antd";

const ReportExport: React.FC = () => {
  return (
    <Card title="报表导出">
      <Empty description="请先完成费用计算后再导出报表" />
    </Card>
  );
};

export default ReportExport;
