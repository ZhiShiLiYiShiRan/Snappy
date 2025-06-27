import os
import httpx
from dotenv import load_dotenv
from pathlib import Path

# 强制加载项目根目录下的 .env 文件
env_path = Path(__file__).resolve().parents[2] / ".env"
print("[debug] looking for .env at:", env_path)

# 强制加载 .env
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    print("[debug] .env loaded ✅")
else:
    print("[debug] ❌ .env file not found at expected path.")

# 显示读取结果
print("[debug] Slack_service的SLACK_BOT_TOKEN =", os.getenv("SLACK_BOT_TOKEN"))



SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_API_URL = "https://slack.com/api"

async def send_image_message_with_buttons(channel: str, image_url: str):
    payload = {
        "channel": channel,
        "text": "请审核以下图片：",
        "blocks": [
            {
                "type": "image",
                "image_url": image_url,
                "alt_text": "审核图片"
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "✅ 通过"},
                        "style": "primary",
                        "value": "approve",
                        "action_id": "approve_action"
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "❌ 不通过"},
                        "style": "danger",
                        "value": "reject",
                        "action_id": "reject_action"
                    }
                ]
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    print("🔑SLACK_BOT_TOKEN =", SLACK_BOT_TOKEN)
 

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{SLACK_API_URL}/chat.postMessage", json=payload, headers=headers)
        
        print("[Slack API response]", response.status_code, response.text)
        return response.json()
    