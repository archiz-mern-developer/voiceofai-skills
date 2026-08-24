#!/usr/bin/env python3
"""Create a new VoiceOfAI voice agent via REST API."""

from __future__ import annotations

import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a VoiceOfAI voice agent")
    parser.add_argument("--name", required=True, help="Agent display name")
    parser.add_argument("--type", default="incoming", choices=["incoming", "flow"], help="Agent type")
    parser.add_argument("--prompt", required=True, help="System prompt")
    parser.add_argument("--first-message", help="First spoken message")
    parser.add_argument("--language", default="en", help="Language code")
    parser.add_argument("--model", default="gpt-4o-mini", help="LLM model")
    args = parser.parse_args()

    api_key = os.environ.get("VOICEOFAI_API_KEY")
    base_url = os.environ.get("VOICEOFAI_BASE_URL", "https://voice.voiceofai.co.in/api/v1").rstrip("/")

    if not api_key:
        print(json.dumps({"error": "VOICEOFAI_API_KEY environment variable is not set."}), file=sys.stderr)
        return 2

    payload = {
        "name": args.name,
        "type": args.type,
        "systemPrompt": args.prompt,
        "firstMessage": args.first_message,
        "language": args.language,
        "llmModel": args.model,
    }

    req = Request(
        f"{base_url}/agents",
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
