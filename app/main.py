from fastapi import FastAPI
from app.api.slack_events import router as slack_router

app = FastAPI()

#注册slack 事件处理路由
app.include_router(slack_router,prefix="/slack")