from fastapi import FastAPI
from app.api.slack_events import router as slack_router
from app.services import slack_service  # ✅ 强制加载 slack_service.py
import os
app = FastAPI()
app.include_router(slack_router)

print("[debug] main.py loaded from", os.path.abspath(__file__))

@app.get("/")
def read_root():
    return {"message": "Slack bot backend running"}
print("🔁 slack_events router 已加载")
print("✅ 注册的路由列表：")
for route in app.routes:
    print(f"• {route.path} [{', '.join(route.methods)}]")

print("✅ 注册的路由：")
print(app.routes)