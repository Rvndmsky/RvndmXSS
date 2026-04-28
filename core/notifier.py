import requests, html
from datetime import datetime
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
def send_telegram(url,payload):
    if "REPLACE_WITH_YOUR_REAL_CHAT_ID" in TELEGRAM_CHAT_ID:
        return
    now = datetime.now()
    safe_url = html.escape(url)
    safe_payload = html.escape(payload)
    msg = f'''<b>🔥 RvndmXSS Confirmed Executable XSS 🔥</b>

<b>Date</b>    : {now.strftime("%Y-%m-%d")}
<b>Time</b>    : {now.strftime("%H:%M:%S")}

<b>URL</b>     : {safe_url}
<b>Payload</b> : {safe_payload}

<b>[Enak Juga Nemu XSS Dibantu Prompt]</b>

<b>Author</b>  : Rvndm | Enggan Ngoding Nyuruh AI saja
<b>Copyright</b> © 2026 RvndmXSS'''
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            data={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode":"HTML"},
            timeout=8
        )
    except:
        pass
