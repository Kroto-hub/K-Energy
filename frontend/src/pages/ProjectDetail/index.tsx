import { Card, Descriptions } from "antd";
import { useParams } from "react-router-dom";

const ProjectDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();

  return (
    <Card title="项目详情">
      <Descriptions bordered column={2}>
        <Descriptions.Item label="项目ID">{id}</Descriptions.Item>
        <Descriptions.Item label="项目名称">示例能源站项目</Descriptions.Item>
        <Descriptions.Item label="地点">北京</Descriptions.Item>
        <Descriptions.Item label="状态">进行中</Descriptions.Item>
        <Descriptions.Item label="创建时间">2026-04-18</Descriptions.Item>
        <Descriptions.Item label="建筑面积">10000 m²</Descriptions.Item>
      </Descriptions>
    </Card>
  );
};

export default ProjectDetail;
