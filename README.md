# FastAPI Example API

這是一個基於 FastAPI 框架的 RESTful API 範例專案，提供了一個可擴展的架構，包含 MongoDB 資料庫連接、API 路由設計、錯誤處理等功能。

## 功能特點

- 基於 FastAPI 的高效能 API 框架
- MongoDB 資料庫整合與單例模式連接管理
- 完整的 CRUD 操作範例
- Pydantic 模型驗證
- Docker 容器化支援
- 結構化日誌系統

## 專案結構
fastapi-example-api/
├── app/
│ ├── api/
│ │ ├── console/
│ │ │ ├── base.py
│ │ │ └── template.py
│ │ ├── init.py
│ │ └── router.py
│ ├── schemas/
│ │ └── base.py
│ ├── services/
│ │ ├── database/
│ │ │ ├── init.py
│ │ │ └── mongo.py
│ ├── utils/
│ │ ├── base.py
│ │ └── logger.py
│ ├── config.py
│ └── main.py
├── logs/
├── Dockerfile
├── requirements.txt
├── run.py
└── build.sh

## 安裝與設定

### 環境需求

- Python 3.12+
- MongoDB

### 本地開發設定

1. 複製專案
bash git clone https://github.com/yourusername/fastapi-example-api.git
cd fastapi-example-api

2. 建立虛擬環境
python -m venv venv
source venv/bin/activate # Linux/Mac
或
venv\Scripts\activate # Windows

3. 安裝依賴
pip install -r requirements.txt

4. 建立 `.env` 檔案並設定環境變數
MONGODB_URL=localhost:27017
MONGODB_DATABASE=example_db
MONGODB_USERNAME=username
MONGODB_PASSWORD=password
MONGODB_AUTH_SOURCE=admin

1. 啟動應用
python run.py

應用將在 http://localhost:5000 運行。


### Docker 部署
1. 建立 Docker 映像
build.sh

2. 運行容器
docker run -p 5000:5000 edgar/fastapi-example:1.0.1

## API 端點

### 基礎端點

- `GET /` - 檢查 API 狀態

### 範本 API

- `GET /api/template` - 獲取所有範本
- `POST /api/template` - 建立新範本
- `PUT /api/template/{id}` - 更新範本
- `DELETE /api/template/{id}` - 刪除範本

## 開發指南

### 新增路由

1. 在 `app/api/console/` 目錄下建立新的路由檔案
2. 在 `app/api/console/__init__.py` 中匯入並註冊新路由
3. 在 `app/api/router.py` 中設定路由前綴和標籤

### 資料模型

使用 Pydantic 建立資料模型，放置在 `app/schemas/` 目錄下。

### 資料庫操作

使用 `app/services/database/mongo.py` 中的 MongoDB 連接類別進行資料庫操作。

## 貢獻指南

1. Fork 專案
2. 建立功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交變更 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 開啟 Pull Request

## 授權

此專案採用 MIT 授權 - 詳見 LICENSE 檔案