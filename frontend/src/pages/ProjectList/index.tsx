import { Button, Card, Table, Space, Tag } from "antd";
import { PlusOutlined } from "@ant-design/icons";
import { useNavigate } from "react-router-dom";
import type { ColumnsType } from "antd/es/table";

interface Project {
  id: string;
  name: string;
  location: string;
  status: string;
  createdAt: string;
}

const mockData: Project[] = [
  {
    id: "1",
    name: "示例能源站项目",
    location: "北京",
    status: "进行中",
    createdAt: "2026-04-18",
  },
];

const columns: ColumnsType<Project> = [
  { title: "项目名称", dataIndex: "name", key: "name" },
  { title: "地点", dataIndex: "location", key: "location" },
  {
    title: "状态",
    dataIndex: "status",
    key: "status",
    render: (status: string) => {
      const color = status === "进行中" ? "blue" : status === "已完成" ? "green" : "default";
      return <Tag color={color}>{status}</Tag>;
    },
  },
  { title: "创建时间", dataIndex: "createdAt", key: "createdAt" },
  {
    title: "操作",
    key: "action",
    render: (_, record) => (
      <Space>
        <a onClick={() => window.location.hash = `/projects/${record.id}`}>查看</a>
        <a onClick={() => window.location.hash = `/projects/${record.id}/station`}>配置</a>
        <a onClick={() => window.location.hash = `/projects/${record.id}/cost`}>费用计算</a>
      </Space>
    ),
  },
];

const ProjectList: React.FC = () => {
  const navigate = useNavigate();

  return (
    <Card
      title="项目列表"
      extra={
        <Button type="primary" icon={<PlusOutlined />}>
          新建项目
        </Button>
      }
    >
      <Table columns={columns} dataSource={mockData} rowKey="id" />
    </Card>
  );
};

export default ProjectList;
