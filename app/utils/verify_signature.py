import os
import hmac
import hashlib
import time
from fastapi import Request

SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

async def verify_slack_signature(request: Request) -> bool:
    timestamp = request.headers.get("X-Slack-Request-Timestamp")
    if not timestamp or abs(time.time() - int(timestamp)) > 60 * 5:
        return False

    request_body = await request.body()
    sig_basestring = f"v0:{timestamp}:{request_body.decode()}"
    my_signature = 'v0=' + hmac.new(
        SLACK_SIGNING_SECRET.encode(),
        sig_basestring.encode(),
        hashlib.sha256
    ).hexdigest()

    slack_signature = request.headers.get("X-Slack-Signature")
    return hmac.compare_digest(my_signature, slack_signature)
