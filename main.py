import requests
from datetime import datetime, timezone
import os

TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

utc_time = datetime.now(timezone.utc).strftime("%H:%M")

new_name = f"🕒 UTC: {utc_time}"

url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}"

headers = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json"
}

requests.patch(
    url,
    headers=headers,
    json={"name": new_name}
)

print("Canal actualizado:", new_name)