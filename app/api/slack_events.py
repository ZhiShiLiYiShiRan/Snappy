from fastapi import APIRouter, Request, Header, HTTPException
from fastapi.responses import JSONResponse
from app.utils.verify_signature import verify_slack_signature
import json
import os

router = APIRouter()

@router.post("/events")
async def handle_slack_events(
    request: Request,
    x_slack_signature: str = Header(None),
    x_slack_request_timestamp: str = Header(None)
):
    body = await request.body()

    if not verify_slack_signature(body, x_slack_request_timestamp, x_slack_signature):
        raise HTTPException(status_code=403, detail="Invalid Slack signature")

    payload = json.loads(body)

    if payload.get("type") == "url_verification":
        return JSONResponse(content={"challenge": payload.get("challenge")})

    # 处理 /record 命令
    if payload.get("command") == "/record":
        return JSONResponse(content={
            "response_type": "in_channel",
            "text": "请选择你的操作：",
            "blocks": [
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "功能测试"},
                            "value": "function_tested"
                        },
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "外观测试"},
                            "value": "appearance_tested"
                        }
                    ]
                }
            ]
        })

    return {"status": "ok"}