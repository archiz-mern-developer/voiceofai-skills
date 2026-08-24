#!/usr/bin/env python3
"""Fetch call, campaign, or summary analytics from VoiceOfAI."""

from __future__ import annotations

import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch analytics from VoiceOfAI")
    parser.add_argument("--type", choices=["calls", "campaigns", "summary"], default="summary", help="Type of analytics")
    parser.add_argument("--days", type=int, default=30, help="Days of history to analyze")
    args = parser.parse_args()

    api_key = os.environ.get("VOICEOFAI_API_KEY")
    base_url = os.environ.get("VOICEOFAI_BASE_URL", "https://voice.voiceofai.co.in/api/v1").rstrip("/")

    if not api_key:
        print(json.dumps({"error": "VOICEOFAI_API_KEY environment variable is not set."}), file=sys.stderr)
        return 2

    if args.type == "calls":
        path = f"/analytics/calls?days={args.days}"
    elif args.type == "campaigns":
        path = "/analytics/campaigns"
    else:
        path = f"/analytics/summary?days={args.days}"

    req = Request(
        f"{base_url}{path}",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        },
        method="GET",
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
