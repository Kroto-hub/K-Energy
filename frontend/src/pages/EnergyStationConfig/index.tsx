import { Card, Form, Input, InputNumber, Select, Button, Space, Divider } from "antd";

const EnergyStationConfig: React.FC = () => {
  const [form] = Form.useForm();

  return (
    <Card title="能源站配置">
      <Form form={form} layout="vertical" style={{ maxWidth: 800 }}>
        <Divider orientation="left">基本信息</Divider>
        <Form.Item label="能源站名称" name="stationName" rules={[{ required: true }]}>
          <Input placeholder="请输入能源站名称" />
        </Form.Item>
        <Form.Item label="建筑面积 (m²)" name="buildingArea" rules={[{ required: true }]}>
          <InputNumber style={{ width: "100%" }} min={0} placeholder="请输入建筑面积" />
        </Form.Item>

        <Divider orientation="left">冷源配置</Divider>
        <Form.Item label="冷水机组类型" name="chillerType">
          <Select placeholder="请选择冷水机组类型">
            <Select.Option value="centrifugal">离心式冷水机组</Select.Option>
            <Select.Option value="screw">螺杆式冷水机组</Select.Option>
            <Select.Option value="absorption">吸收式冷水机组</Select.Option>
          </Select>
        </Form.Item>
        <Form.Item label="制冷量 (kW)" name="coolingCapacity">
          <InputNumber style={{ width: "100%" }} min={0} placeholder="请输入制冷量" />
        </Form.Item>
        <Form.Item label="额定 COP" name="ratedCOP">
          <InputNumber style={{ width: "100%" }} min={0} step={0.1} placeholder="请输入额定COP" />
        </Form.Item>

        <Divider orientation="left">热源配置</Divider>
        <Form.Item label="热源类型" name="heatingType">
          <Select placeholder="请选择热源类型">
            <Select.Option value="boiler">燃气锅炉</Select.Option>
            <Select.Option value="heatPump">空气源热泵</Select.Option>
            <Select.Option value="gsHeatPump">地源热泵</Select.Option>
          </Select>
        </Form.Item>
        <Form.Item label="制热量 (kW)" name="heatingCapacity">
          <InputNumber style={{ width: "100%" }} min={0} placeholder="请输入制热量" />
        </Form.Item>

        <Form.Item>
          <Space>
            <Button type="primary" htmlType="submit">保存配置</Button>
            <Button>取消</Button>
          </Space>
        </Form.Item>
      </Form>
    </Card>
  );
};

export default EnergyStationConfig;
