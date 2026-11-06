#!/usr/bin/env python3
"""Send the text from argv[1] to Telegram. Uses TG_BOT_TOKEN, TG_CHAT_ID and TG_THREAD_ID."""
import json
import os
import sys
import urllib.error
import urllib.request

LIMIT = 4000


def main():
    token = os.environ["TG_BOT_TOKEN"]
    payload = {
        "chat_id": os.environ["TG_CHAT_ID"],
        "message_thread_id": int(os.environ["TG_THREAD_ID"]),
        "text": sys.argv[1][:LIMIT],
        "disable_web_page_preview": True,
    }
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    try:
        urllib.request.urlopen(req, timeout=30).close()
    except urllib.error.HTTPError as e:
        print(f"notify_telegram: HTTP {e.code}", file=sys.stderr)
        return 1
    except urllib.error.URLError:
        # The exception text may include the URL with the token, so don't print it
        print("notify_telegram: network error", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
