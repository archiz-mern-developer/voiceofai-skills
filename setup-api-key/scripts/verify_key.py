#!/usr/bin/env python3
"""Verify VOICEOFAI_API_KEY against the VoiceOfAI health/credits endpoint."""

from __future__ import annotations

import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main() -> int:
    api_key = os.environ.get("VOICEOFAI_API_KEY")
    base_url = os.environ.get("VOICEOFAI_BASE_URL", "https://voice.voiceofai.co.in/api/v1").rstrip("/")

    if not api_key:
        print(json.dumps({"valid": False, "error": "VOICEOFAI_API_KEY environment variable is not set."}), file=sys.stderr)
        return 2

    req = Request(
        f"{base_url}/credits/balance",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        },
        method="GET",
    )

    try:
        with urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(json.dumps({"valid": True, "base_url": base_url, "response": data}, indent=2))
            return 0
    except HTTPError as exc:
        err_body = exc.read().decode("utf-8")
        print(json.dumps({"valid": False, "status_code": exc.code, "error": err_body}, indent=2), file=sys.stderr)
        return 1
    except URLError as exc:
        print(json.dumps({"valid": False, "error": f"Failed to reach API at {base_url}: {exc.reason}"}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
