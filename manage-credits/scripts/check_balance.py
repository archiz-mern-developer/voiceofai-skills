#!/usr/bin/env python3
"""Check VoiceOfAI credit balance and usage history."""

from __future__ import annotations

import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main() -> int:
    parser = argparse.ArgumentParser(description="Check VoiceOfAI credit balance and usage")
    parser.add_argument("--days", type=int, default=30, help="Days of history to fetch (1-90)")
    args = parser.parse_args()

    api_key = os.environ.get("VOICEOFAI_API_KEY")
    base_url = os.environ.get("VOICEOFAI_BASE_URL", "https://voice.voiceofai.co.in/api/v1").rstrip("/")

    if not api_key:
        print(json.dumps({"error": "VOICEOFAI_API_KEY environment variable is not set."}), file=sys.stderr)
        return 2

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
    }

    try:
        # Fetch balance
        req_bal = Request(f"{base_url}/credits/balance", headers=headers, method="GET")
        with urlopen(req_bal, timeout=10) as resp:
            balance_data = json.loads(resp.read().decode("utf-8"))

        # Fetch usage
        req_usage = Request(f"{base_url}/credits/usage?days={args.days}", headers=headers, method="GET")
        with urlopen(req_usage, timeout=10) as resp:
            usage_data = json.loads(resp.read().decode("utf-8"))

        result = {
            "balance": balance_data,
            "usage": usage_data,
        }
        print(json.dumps(result, indent=2))
        return 0
    except HTTPError as exc:
        print(json.dumps({"status_code": exc.code, "error": exc.read().decode("utf-8")}, indent=2), file=sys.stderr)
        return 1
    except URLError as exc:
        print(json.dumps({"error": str(exc.reason)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
