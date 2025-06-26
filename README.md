# Slack Bot 项目

一个使用 FastAPI + MongoDB 构建的 Slack 机器人，支持按钮交互、图片记录、CSV 导出，部署于 Railway。

## 快速启动
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 文件结构说明
- `app/`：主代码目录，含路由、服务、模型、数据库等模块
- `.env.example`：参考用环境变量
- `Procfile`：部署启动命令