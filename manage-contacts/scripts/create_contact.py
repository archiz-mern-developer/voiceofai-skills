#!/usr/bin/env python3
"""Create a single contact in VoiceOfAI CRM."""

from __future__ import annotations

import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a CRM contact")
    parser.add_argument("--phone", required=True, help="Phone number in E.164 format")
    parser.add_argument("--first-name", help="First name")
    parser.add_argument("--last-name", help="Last name")
    parser.add_argument("--email", help="Email address")
    parser.add_argument("--company", help="Company name")
    parser.add_argument("--tags", help="Comma-separated tags (e.g. 'vip,lead')")
    args = parser.parse_args()

    api_key = os.environ.get("VOICEOFAI_API_KEY")
    base_url = os.environ.get("VOICEOFAI_BASE_URL", "https://voice.voiceofai.co.in/api/v1").rstrip("/")

    if not api_key:
        print(json.dumps({"error": "VOICEOFAI_API_KEY environment variable is not set."}), file=sys.stderr)
        return 2

    tags_list = [t.strip() for t in args.tags.split(",")] if args.tags else None

    payload = {
        "phone": args.phone,
        "firstName": args.first_name,
        "lastName": args.last_name,
        "email": args.email,
        "company": args.company,
        "tags": tags_list,
    }

    req = Request(
        f"{base_url}/contacts",
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
