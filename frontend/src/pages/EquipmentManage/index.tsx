import { Card, Table, Button, Space } from "antd";
import { PlusOutlined } from "@ant-design/icons";
import type { ColumnsType } from "antd/es/table";

interface Equipment {
  id: string;
  name: string;
  type: string;
  brand: string;
  capacity: number;
  unit: string;
}

const mockData: Equipment[] = [];

const columns: ColumnsType<Equipment> = [
  { title: "设备名称", dataIndex: "name", key: "name" },
  { title: "类型", dataIndex: "type", key: "type" },
  { title: "品牌", dataIndex: "brand", key: "brand" },
  { title: "容量", dataIndex: "capacity", key: "capacity" },
  { title: "单位", dataIndex: "unit", key: "unit" },
  {
    title: "操作",
    key: "action",
    render: () => (
      <Space>
        <a>编辑</a>
        <a>删除</a>
      </Space>
    ),
  },
];

const EquipmentManage: React.FC = () => {
  return (
    <Card
      title="设备管理"
      extra={
        <Button type="primary" icon={<PlusOutlined />}>
          添加设备
        </Button>
      }
    >
      <Table columns={columns} dataSource={mockData} rowKey="id" />
    </Card>
  );
};

export default EquipmentManage;
