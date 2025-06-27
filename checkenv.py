# checkenv.py
from dotenv import load_dotenv
import os

print("Running from:", os.getcwd())
load_dotenv()

print("SLACK_BOT_TOKEN =", os.getenv("SLACK_BOT_TOKEN"))
print("SLACK_SIGNING_SECRET =", os.getenv("SLACK_SIGNING_SECRET"))
