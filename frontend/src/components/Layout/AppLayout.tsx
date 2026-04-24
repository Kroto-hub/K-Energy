import { useState, useEffect } from "react";
import { Outlet, useNavigate, useLocation, matchPath } from "react-router-dom";
import { Layout, Menu, theme, Space, Tabs, message, Modal, Form, Input, Tag } from "antd";
import {
  DashboardOutlined,
  ProjectOutlined,
  DatabaseOutlined,
  PlusOutlined,
  CloudOutlined,
  BuildOutlined,
  ToolOutlined,
  LineChartOutlined,
  DollarOutlined,
  ApartmentOutlined,
  BorderOutlined,
  BarsOutlined,
  BarChartOutlined,
  CalendarOutlined,
} from "@ant-design/icons";

import { getProjects, createProject, getProjectBuildings } from "../../api/projects";
import { Project, ProjectBuilding } from "../../types/project";

const { Header, Sider, Content } = Layout;

const AppLayout: React.FC = () => {
  const [collapsed, setCollapsed] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();
  const [projects, setProjects] = useState<Project[]>([]);
  const [currentProjectBuildings, setCurrentProjectBuildings] = useState<ProjectBuilding[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [form] = Form.useForm();
  const [submitting, setSubmitting] = useState(false);

  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  const fetchProjects = async () => {
    try {
      const data = await getProjects();
      setProjects(data);
    } catch (error: any) {
      console.error("获取项目列表失败", error);
    }
  };

  useEffect(() => {
    fetchProjects();
  }, []);

  const fetchCurrentProjectBuildings = async (currentProjectId?: string) => {
    if (!currentProjectId) {
      setCurrentProjectBuildings([]);
      return;
    }

    try {
      const buildings = await getProjectBuildings(currentProjectId);
      setCurrentProjectBuildings(buildings);
    } catch (error) {
      setCurrentProjectBuildings([]);
    }
  };

  const handleCreate = async (values: any) => {
    try {
      setSubmitting(true);
      const payload = {
        name: values.name || "",
        description: values.description || "",
      };
      const res = await createProject(payload);
      message.success("项目创建成功");
      setIsModalOpen(false);
      form.resetFields();
      await fetchProjects();
      navigate(`/projects/${res.id}/buildings`);
    } catch (error: any) {
      message.error(error.message || "创建项目失败");
    } finally {
      setSubmitting(false);
    }
  };

  const projectMatch = matchPath("/projects/:id/*", location.pathname);
  const projectId = projectMatch?.params?.id;
  const buildingRouteMatch = matchPath("/projects/:id/buildings/:buildingId/*", location.pathname);
  const currentBuildingId = buildingRouteMatch?.params?.buildingId;
  const currentProjectMenuKey = projectId ? `/projects/${projectId}` : undefined;

  useEffect(() => {
    fetchCurrentProjectBuildings(projectId);
  }, [projectId]);

  const getSelectedKeys = () => {
    const keys: string[] = [];

    if (location.pathname.startsWith("/database")) {
      return ["/database"];
    }

    if (currentProjectMenuKey) {
      keys.push(currentProjectMenuKey);
    }

    if (currentBuildingId) {
      keys.push(`building:${currentBuildingId}`);
      return keys;
    }
    if (projectId && location.pathname.startsWith(`/projects/${projectId}/weather`)) {
      keys.push(`/projects/${projectId}/weather`);
      return keys;
    }
    if (projectId && location.pathname.startsWith(`/projects/${projectId}/buildings`)) {
      keys.push(`/projects/${projectId}/buildings`);
      return keys;
    }
    if (projectId && location.pathname.startsWith(`/projects/${projectId}/station`)) {
      keys.push(`/projects/${projectId}/station`);
      return keys;
    }
    if (projectId && location.pathname.startsWith(`/projects/${projectId}/construction-templates`)) {
      keys.push(`/projects/${projectId}/construction-templates`);
      return keys;
    }
    if (projectId && location.pathname.startsWith(`/projects/${projectId}/schedules`)) {
      keys.push(`/projects/${projectId}/schedules`);
      return keys;
    }
    if (projectId && location.pathname.startsWith(`/projects/${projectId}/schemes`)) {
      keys.push(`/projects/${projectId}/schemes`);
      return keys;
    }
    if (projectId && location.pathname.startsWith(`/projects/${projectId}/load`)) {
      keys.push(`/projects/${projectId}/load`);
      return keys;
    }
    if (projectId && location.pathname.startsWith(`/projects/${projectId}/cost`)) {
      keys.push(`/projects/${projectId}/cost`);
      return keys;
    }
    if (projectId) {
      keys.push(`/projects/${projectId}/buildings`);
      return keys;
    }
    return ["/projects"];
  };

  const menuItems = [
    {
      key: "/projects",
      icon: <DashboardOutlined />,
      label: "项目管理",
    },
    {
      key: "project_list_group",
      type: "group" as const,
      label: "项目列表",
      children: [
        ...projects.map((p) => ({
          key: `/projects/${p.id}`,
          icon: <ProjectOutlined />,
          label: (
            <Space size={8}>
              <span>{p.name}</span>
              {projectId === p.id ? (
                <Tag color="blue" style={{ marginInlineEnd: 0, borderRadius: 999 }}>
                  当前
                </Tag>
              ) : null}
            </Space>
          ),
        })),
        {
          key: "new_project",
          icon: <PlusOutlined />,
          label: "新建项目",
        },
      ],
    },
    ...(projectId
      ? [
          {
            type: "divider" as const,
          },
          {
            key: "current_project_group",
            type: "group" as const,
            label: "当前项目",
            children: [
              {
                key: `/projects/${projectId}/weather`,
                icon: <CloudOutlined />,
                label: "气象与计算设置",
              },
              {
                key: `/projects/${projectId}/buildings`,
                icon: <ApartmentOutlined />,
                label: "楼栋管理",
              },
              ...currentProjectBuildings.map((building) => ({
                key: `building:${building.id}`,
                icon: <BuildOutlined />,
                label: building.name,
              })),
              {
                key: `new_building:${projectId}`,
                icon: <PlusOutlined />,
                label: "新建楼栋",
              },
              {
                key: `/projects/${projectId}/construction-templates`,
                icon: <BorderOutlined />,
                label: "围护模板库",
              },
              {
                key: `/projects/${projectId}/schedules`,
                icon: <CalendarOutlined />,
                label: "计划表",
              },
              {
                key: `/projects/${projectId}/station`,
                icon: <ToolOutlined />,
                label: "设备选型",
              },
              {
                key: `/projects/${projectId}/schemes`,
                icon: <BarChartOutlined />,
                label: "方案对比",
              },
              {
                key: `/projects/${projectId}/cost`,
                icon: <DollarOutlined />,
                label: "费用及初投资",
              },
            ],
          },
        ]
      : []),
    {
      type: "divider" as const,
    },
    {
      key: "/database",
      icon: <DatabaseOutlined />,
      label: "数据库修改",
    },
  ];

  const handleMenuClick = ({ key }: { key: string }) => {
    if (key === "new_project") {
      setIsModalOpen(true);
    } else if (key.startsWith("new_building:")) {
      navigate(`/projects/${projectId}/buildings`);
    } else if (key.startsWith("building:")) {
      const buildingId = key.split(":")[1];
      navigate(`/projects/${projectId}/buildings/${buildingId}/model`);
    } else if (key.startsWith("/projects/") && key !== "/projects") {
      if (key === `/projects/${projectId}`) {
        navigate(`/projects/${projectId}/buildings`);
      } else {
        navigate(key);
      }
    } else {
      navigate(key);
    }
  };

  const projectTabs = [
    { key: "weather", label: "气象城市", icon: <CloudOutlined /> },
    { key: "buildings", label: "楼栋管理", icon: <ApartmentOutlined /> },
    { key: "construction-templates", label: "围护模板库", icon: <BorderOutlined /> },
    { key: "schedules", label: "计划表", icon: <CalendarOutlined /> },
    { key: "station", label: "设备选型", icon: <ToolOutlined /> },
    { key: "schemes", label: "方案对比", icon: <BarChartOutlined /> },
    { key: "load", label: "项目汇总结果", icon: <LineChartOutlined /> },
    { key: "cost", label: "费用及初投资计算", icon: <DollarOutlined /> },
  ];

  const buildingTabs = [
    { key: "model", label: "建筑模型", icon: <BuildOutlined /> },
    { key: "floors", label: "楼层参数", icon: <BarsOutlined /> },
    { key: "envelope", label: "围护结构", icon: <BorderOutlined /> },
    { key: "load", label: "负荷结果", icon: <LineChartOutlined /> },
  ];

  const isBuildingScope = !!currentBuildingId;
  const currentTab = isBuildingScope
    ? buildingTabs.find((tab) => location.pathname.includes(`/${tab.key}`))?.key || "model"
    : projectTabs.find((tab) => location.pathname.includes(`/${tab.key}`))?.key || "buildings";

  const handleTabChange = (key: string) => {
    if (projectId && currentBuildingId) {
      navigate(`/projects/${projectId}/buildings/${currentBuildingId}/${key}`);
    } else if (projectId) {
      navigate(`/projects/${projectId}/${key}`);
    }
  };

  return (
    <Layout style={{ minHeight: "100vh" }}>
      <Sider collapsible collapsed={collapsed} onCollapse={setCollapsed}>
        <div
          style={{
            height: 32,
            margin: 16,
            color: "#fff",
            fontSize: collapsed ? 14 : 18,
            fontWeight: "bold",
            textAlign: "center",
            lineHeight: "32px",
            whiteSpace: "nowrap",
            overflow: "hidden",
          }}
        >
          {collapsed ? "KE" : "K-Energy"}
        </div>
        <Menu theme="dark" selectedKeys={getSelectedKeys()} mode="inline" items={menuItems} onClick={handleMenuClick} />
      </Sider>
      <Layout>
        <Header
          style={{
            padding: projectId ? "0 24px 0 0" : "0 24px",
            background: colorBgContainer,
            display: "flex",
            alignItems: "center",
            boxShadow: "0 1px 4px rgba(0,21,41,.08)",
            zIndex: 1,
          }}
        >
          {projectId ? (
            <Tabs
              activeKey={currentTab}
              onChange={handleTabChange}
              items={(isBuildingScope ? buildingTabs : projectTabs).map((tab) => ({
                key: tab.key,
                label: (
                  <span>
                    {tab.icon}
                    {tab.label}
                  </span>
                ),
              }))}
              style={{ flex: 1, marginBottom: "-16px", paddingLeft: "24px" }}
            />
          ) : (
            <div style={{ fontSize: 16, fontWeight: 500 }}>K-Energy 能源计算系统</div>
          )}
        </Header>
        <Content
          style={{
            margin: 16,
            padding: 24,
            background: colorBgContainer,
            borderRadius: borderRadiusLG,
            minHeight: 280,
          }}
        >
          <Outlet
            context={{
              projects,
              refreshProjects: fetchProjects,
              buildings: currentProjectBuildings,
              refreshBuildings: () => fetchCurrentProjectBuildings(projectId),
            }}
          />
        </Content>
      </Layout>

      <Modal
        title={<span style={{ fontWeight: 600 }}>新建能源项目</span>}
        open={isModalOpen}
        onCancel={() => setIsModalOpen(false)}
        confirmLoading={submitting}
        okText="创建项目"
        cancelText="取消"
        centered
        width={600}
        onOk={() => form.submit()}
      >
        <Form form={form} layout="vertical" onFinish={handleCreate} style={{ marginTop: 24 }}>
          <Form.Item name="name" label="项目名称" rules={[{ required: true, message: "请输入项目名称" }]}>
            <Input size="large" placeholder="例如：上海某数据中心冷热源项目" />
          </Form.Item>
          <Form.Item name="description" label="项目描述">
            <Input.TextArea rows={3} placeholder="项目相关详细信息和备注..." />
          </Form.Item>
        </Form>
      </Modal>
    </Layout>
  );
};

export default AppLayout;
