from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from fastapi import Body
from app.utils.verify_signature import verify_slack_signature
from app.services.slack_service import send_image_message_with_buttons
import json
import os

router = APIRouter(
    prefix="/slack",
    tags=["Slack"]
)
print("[debug] .env SLACK_BOT_TOKEN =", os.getenv("SLACK_BOT_TOKEN"))
@router.post("/interactions")
async def slack_interactions(request: Request):
    if not await verify_slack_signature(request):
        return JSONResponse(content={"error": "invalid signature"}, status_code=status.HTTP_403_FORBIDDEN)

    form = await request.form()
    payload = json.loads(form["payload"])

    action_id = payload["actions"][0]["action_id"]
    user = payload["user"]["username"]

    if action_id == "approve_action":
        response_text = f"✅ {user} 通过了此图片"
    elif action_id == "reject_action":
        response_text = f"❌ {user} 拒绝了此图片"
    else:
        response_text = "⚠️ 未知操作"

    return JSONResponse(content={"text": response_text})


@router.get("/send-test-message",tags=["Test"])
@router.post("/send-test-message",tags=["Test"])
async def send_test(dummy: dict = Body(default={})):
    print("🧪 send_test 被调用")
    res = await send_image_message_with_buttons(
        channel="C092X77JQV7",  # ✅ 使用你的 Slack 频道 ID
        image_url="https://via.placeholder.com/300"
    )
    return res

print("✅ slack_events.py 已加载")