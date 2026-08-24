#!/usr/bin/env python3
"""Trigger an outbound call using VoiceOfAI."""

from __future__ import annotations

import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main() -> int:
    parser = argparse.ArgumentParser(description="Trigger an outbound VoiceOfAI call")
    parser.add_argument("--agent-id", required=True, help="Voice agent UUID")
    parser.add_argument("--to", required=True, help="Recipient phone number (E.164 format)")
    parser.add_argument("--engine", default="voiceofai", help="Telephony engine")
    parser.add_argument("--from-number", help="Caller ID phone number")
    parser.add_argument("--metadata", help="JSON metadata string")
    parser.add_argument("--scheduled-at", help="ISO-8601 scheduled timestamp")
    args = parser.parse_args()

    api_key = os.environ.get("VOICEOFAI_API_KEY")
    base_url = os.environ.get("VOICEOFAI_BASE_URL", "https://voice.voiceofai.co.in/api/v1").rstrip("/")

    if not api_key:
        print(json.dumps({"error": "VOICEOFAI_API_KEY environment variable is not set."}), file=sys.stderr)
        return 2

    metadata_dict = None
    if args.metadata:
        try:
            metadata_dict = json.loads(args.metadata)
        except ValueError:
            print(json.dumps({"error": "Invalid JSON string passed to --metadata."}), file=sys.stderr)
            return 2

    payload = {
        "agentId": args.agent_id,
        "toNumber": args.to,
        "engine": args.engine,
        "fromNumber": args.from_number,
        "metadata": metadata_dict,
        "scheduledAt": args.scheduled_at,
    }
    # Drop None keys
    payload = {k: v for k, v in payload.items() if v is not None}

    req = Request(
        f"{base_url}/calls",
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
