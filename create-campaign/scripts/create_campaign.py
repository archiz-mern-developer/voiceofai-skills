#!/usr/bin/env python3
"""Create a new VoiceOfAI campaign."""

from __future__ import annotations

import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a VoiceOfAI bulk campaign")
    parser.add_argument("--name", required=True, help="Campaign name")
    parser.add_argument("--agent-id", required=True, help="Voice agent UUID")
    parser.add_argument("--engine", default="voiceofai", help="Telephony engine")
    parser.add_argument("--max-concurrent", type=int, default=5, help="Max concurrent calls")
    args = parser.parse_args()

    api_key = os.environ.get("VOICEOFAI_API_KEY")
    base_url = os.environ.get("VOICEOFAI_BASE_URL", "https://voice.voiceofai.co.in/api/v1").rstrip("/")

    if not api_key:
        print(json.dumps({"error": "VOICEOFAI_API_KEY environment variable is not set."}), file=sys.stderr)
        return 2

    # Multipart form data creation or plain json payload
    payload = {
        "name": args.name,
        "agentId": args.agent_id,
        "engine": args.engine,
        "maxConcurrentCalls": args.max_concurrent,
    }

    req = Request(
        f"{base_url}/campaigns",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )

    try:
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(json.dumps(data, indent=2))
            return 0
    except HTTPError as exc:
        print(json.dumps({"status_code": exc.code, "error": exc.read().decode("utf-8")}, indent=2), file=sys.stderr)
        return 1
    except URLError as exc:
        print(json.dumps({"error": str(exc.reason)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
