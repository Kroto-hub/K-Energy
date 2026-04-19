# K-Energy 能源计算软件 - 架构规划

> 更新时间：2026-04-18 | 状态：阶段一已完成

***

## 一、项目现状

项目 `e:\AI_software_develope\K-Energy` 基于 EnergyPlus v26.1.0-6f2e40d102 构建，阶段一（项目骨架搭建）已全部完成。前后端均可正常运行并成功联调。

**已完成：**

* ✅ 后端 FastAPI 项目结构 + 数据库 + API

* ✅ 前端 React + TypeScript + Ant Design 项目

* ✅ 前后端联调（CORS + Vite 代理）

* ✅ SQLite 数据库 + 5 张 SQLAlchemy 数据模型

* ✅ EnergyPlus 集成层骨架（runner/idf\_builder/result\_parser/cop\_calculator/weather\_manager）

* ✅ 启动脚本 `start.bat`

***

## 二、技术栈

| 层    | 方案                              | 说明                      |
| ---- | ------------------------------- | ----------------------- |
| 后端   | Python + FastAPI                | 直接调用 `pyenergyplus` API |
| 前端   | React + TypeScript + Ant Design | 表单 + ECharts 图表         |
| 数据库  | SQLite（开发）→ PostgreSQL（生产）      | SQLAlchemy ORM          |
| 构建工具 | Vite（前端）+ Uvicorn（后端）           | 热更新开发                   |

**核心依赖：** `fastapi`, `uvicorn`, `sqlalchemy`, `alembic`, `pandas`, `eppy`, `react`, `antd`, `echarts`, `axios`, `zustand`

***

## 三、实际项目文件结构

```
K-Energy/
├── EnergyPlus/                    # EnergyPlus v26.1.0（不改动）
├── backend/                       # Python 后端 ✅
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                # FastAPI 入口（含 CORS、lifespan）
│   │   ├── config.py              # 配置（EnergyPlus路径、数据库URL、CORS）
│   │   ├── database.py            # SQLAlchemy 引擎 + 会话 + Base
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── project.py         # Project, EnergyStation, Equipment, LoadProfile, CalculationResult
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── project.py         # ProjectCreate/Update/Response
│   │   │   ├── energy_station.py  # EnergyStationCreate/Update/Response
│   │   │   ├── equipment.py       # EquipmentCreate/Update/Response
│   │   │   └── calculation.py     # CalculationResultResponse
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── router.py          # 路由注册（含 health 端点）
│   │   │   └── projects.py        # 项目/能源站/设备 CRUD API
│   │   ├── services/
│   │   │   └── __init__.py
│   │   ├── energyplus/            # EnergyPlus 集成层骨架
│   │   │   ├── __init__.py
│   │   │   ├── runner.py          # 命令行调用封装
│   │   │   ├── idf_builder.py     # IDF 文件动态生成
│   │   │   ├── result_parser.py   # CSV/ESO 结果解析
│   │   │   ├── cop_calculator.py  # 双二次曲线 COP 计算
│   │   │   └── weather_manager.py # 气象数据管理
│   │   └── utils/
│   │       └── __init__.py
│   ├── alembic/
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions/
│   ├── alembic.ini
│   ├── requirements.txt
│   └── pyproject.toml
├── frontend/                      # React 前端 ✅
│   ├── src/
│   │   ├── main.tsx               # 入口（中文 ConfigProvider + React Router）
│   │   ├── index.css
│   │   ├── App.tsx                # 路由配置（7个页面路由）
│   │   ├── api/
│   │   │   ├── client.ts          # Axios 实例（自动代理到后端）
│   │   │   └── projects.ts        # API 调用封装
│   │   ├── components/
│   │   │   ├── Layout/
│   │   │   │   └── AppLayout.tsx  # 侧边栏布局（Ant Design Layout）
│   │   │   ├── LoadChart/         # 8760h 负荷曲线（待开发）
│   │   │   ├── CostTable/         # 费用明细表（待开发）
│   │   │   └── EquipmentSelector/ # 设备选择器（待开发）
│   │   ├── pages/
│   │   │   ├── ProjectList/       # 项目列表（含示例数据）
│   │   │   ├── ProjectDetail/     # 项目详情
│   │   │   ├── EnergyStationConfig/  # 能源站配置表单
│   │   │   ├── EquipmentManage/   # 设备管理
│   │   │   ├── LoadAnalysis/      # 负荷分析（空状态页）
│   │   │   ├── CostCalculation/   # 费用计算（空状态页）
│   │   │   └── ReportExport/      # 报表导出（空状态页）
│   │   ├── stores/
│   │   │   └── projectStore.ts    # Zustand 状态管理
│   │   ├── types/
│   │   │   └── project.ts         # TypeScript 类型定义
│   │   └── utils/
│   ├── index.html
│   ├── vite.config.ts             # Vite 配置（含 /api 代理到 localhost:8000）
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── package.json
├── data/                          # 数据文件 ✅
│   ├── k_energy.db                # SQLite 数据库（已创建，含 projects 表 1 条测试数据）
│   ├── weather/                   # 气象数据(.epw)（待填充）
│   ├── equipment_db/              # 设备参数（待从国内数据库导入）
│   └── templates/                 # IDF 模板（待创建）
├── start.bat                      # 一键启动脚本 ✅
└── check_db.py                    # 数据库查看脚本 ✅
```

***

## 四、数据库模型

### 5 张核心表

| 表名                       | 说明    | 主要字段                                                                                                                                    |
| ------------------------ | ----- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **projects**             | 项目管理  | id, name, location, building\_area, description, status, weather\_file                                                                  |
| **energy\_stations**     | 能源站配置 | id, project\_id, chiller\_type, cooling\_capacity, rated\_cop, heating\_type, 电价/气价/水价, 安装费比例                                           |
| **equipment**            | 设备库   | id, name, category, brand, model, capacity, rated\_cop, performance\_curves(JSON), price                                                |
| **load\_profiles**       | 负荷曲线  | id, station\_id, cooling\_loads(JSON), heating\_loads(JSON), cop\_values, outdoor\_temps                                                |
| **calculation\_results** | 计算结果  | id, project\_id, station\_id, equipment\_cost, installation\_cost, total\_initial\_cost, annual\_electricity\_cost, total\_annual\_cost |

### 初投资计算字段（energy\_stations 表）

* `installation_rate`：安装费比例（默认 20%）

* `pipe_rate`：管道及附属比例（默认 15%）

* `electrical_rate`：电气自控比例（默认 12%）

* `other_rate`：其他费用比例（默认 8%）

### 费用计算字段（energy\_stations 表）

* `electricity_price`：电价（默认 0.85 元/kWh）

* `peak_electricity_price`：峰时电价（默认 1.2）

* `flat_electricity_price`：平时电价（默认 0.85）

* `valley_electricity_price`：谷时电价（默认 0.4）

* `gas_price`：天然气价（默认 3.5 元/m³）

* `water_price`：水价（默认 6.0 元/吨）

* `maintenance_rate`：维护费比例（默认 3%/年）

***

## 五、API 端点

### 项目与能源站

| 方法     | 路径                              | 说明        |
| ------ | ------------------------------- | --------- |
| GET    | `/api/v1/health`                | 健康检查      |
| GET    | `/api/v1/projects`              | 项目列表      |
| POST   | `/api/v1/projects`              | 创建项目      |
| GET    | `/api/v1/projects/:id`          | 项目详情      |
| PUT    | `/api/v1/projects/:id`          | 更新项目      |
| DELETE | `/api/v1/projects/:id`          | 删除项目      |
| GET    | `/api/v1/projects/:id/stations` | 项目下的能源站列表 |
| POST   | `/api/v1/projects/:id/stations` | 创建能源站     |
| PUT    | `/api/v1/stations/:id`          | 更新能源站     |

### 设备管理

| 方法     | 路径                      | 说明                   |
| ------ | ----------------------- | -------------------- |
| GET    | `/api/v1/equipment`     | 设备列表（支持 category 过滤） |
| POST   | `/api/v1/equipment`     | 创建设备                 |
| PUT    | `/api/v1/equipment/:id` | 更新设备                 |
| DELETE | `/api/v1/equipment/:id` | 删除设备                 |

### 待开发

* `/api/v1/calculation/` - 计算触发与结果查询

* `/api/v1/load/` - 负荷数据查询

* `/api/v1/report/` - 报表导出

***

## 六、EnergyPlus 集成方案

### 6.1 调用流程

```
用户输入参数 → IDFBuilder 生成 IDF → EnergyPlusRunner 调用 energyplus.exe → ResultParser 解析 CSV → pandas 处理 → 费用计算
```

### 6.2 8760h 负荷计算

* **IDF 生成**：`idf_builder.py` 支持 Building/Zone/Sizing:Zone 等基础对象

* **运行方式**：命令行 `energyplus.exe -w weather.epw -d output_dir -r input.idf`

* **结果解析**：`result_parser.py` 解析 CSV，提取冷/热负荷和 HVAC 电耗

* **关键变量**：`Zone Ideal Loads Supply Air Total Cooling/Heating Energy`

### 6.3 COP 计算

* **方法一（已实现）**：双二次曲线 `cop_calculator.py`，COP = f(T\_chw, T\_cond) × PLR修正

* **方法二**：EnergyPlus 性能曲线（通过 `Chiller:Electric:EIR` 模拟）

* **方法三**：国内设备数据库查表（预留 `equipment_db/` 目录）

### 6.4 费用计算

```
初投资 = Σ(设备费) × (1 + 安装率 + 管道率 + 电气率 + 其他率)
年运行费 = Σ(逐时电耗 × 对应时段电价) + 燃气费 + 水费 + 维护费
```

***

## 七、前端页面规划

| 页面    | 路由                      | 状态    | 功能                 |
| ----- | ----------------------- | ----- | ------------------ |
| 项目管理  | `/projects`             | ✅ 骨架  | 列表 + 新建 + 查看       |
| 项目详情  | `/projects/:id`         | ✅ 骨架  | Descriptions 展示    |
| 能源站配置 | `/projects/:id/station` | ✅ 骨架  | 设备选型表单             |
| 设备管理  | `/equipment`            | ✅ 骨架  | 设备库管理              |
| 负荷分析  | `/projects/:id/load`    | ⏳ 空状态 | 8760h 曲线图（ECharts） |
| 费用计算  | `/projects/:id/cost`    | ⏳ 空状态 | 初投资+年运行费计算         |
| 报表导出  | `/projects/:id/report`  | ⏳ 空状态 | Excel 导出           |

***

## 八、后续实施步骤

### 阶段二：核心 API 与业务逻辑

1. 实现能源站与项目的关联 API
2. 实现计算触发 API（`/api/v1/calculation/run`）
3. 实现费用计算服务（`services/cost_calculator.py`）
4. 实现初投资和年运行费用计算逻辑

### 阶段三：EnergyPlus 完整集成

1. 完善 IDFBuilder（支持围护结构、设备、Output:Variable）
2. 实现完整模拟流程（含气象数据选择）
3. 实现 LoadProfile 的存储与查询
4. 实现 COP 逐时计算与存储

### 阶段四：费用计算

1. 实现分时电价计算
2. 实现燃气费计算
3. 实现维护费计算
4. 前后端对接计算流程

### 阶段五：前端页面

1. 项目管理页面（连接真实 API）
2. 能源站配置页面（连接真实 API）
3. 负荷分析页面（ECharts 8760h 曲线）
4. 费用计算结果页面（费用明细表 + 饼图）
5. 报表导出功能

### 阶段六：优化完善

1. 设备数据库导入功能（CSV/Excel → SQLite）
2. 多方案对比功能
3. 计算任务异步化（BackgroundTasks）
4. 错误处理与日志

