#!/usr/bin/env python3
"""Bulk import contacts from a JSON file into VoiceOfAI CRM."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main() -> int:
    parser = argparse.ArgumentParser(description="Bulk import contacts from JSON file")
    parser.add_argument("--json-file", required=True, help="Path to JSON file containing array of contacts")
    parser.add_argument("--skip-duplicates", action="store_true", default=True, help="Skip duplicate phone numbers")
    args = parser.parse_args()

    api_key = os.environ.get("VOICEOFAI_API_KEY")
    base_url = os.environ.get("VOICEOFAI_BASE_URL", "https://voice.voiceofai.co.in/api/v1").rstrip("/")

    if not api_key:
        print(json.dumps({"error": "VOICEOFAI_API_KEY environment variable is not set."}), file=sys.stderr)
        return 2

    json_path = Path(args.json_file)
    if not json_path.exists():
        print(json.dumps({"error": f"JSON file not found: {args.json_file}"}), file=sys.stderr)
        return 2

    try:
        contacts = json.loads(json_path.read_text(encoding="utf-8"))
        if not isinstance(contacts, list):
            print(json.dumps({"error": "JSON file must contain an array of contact objects."}), file=sys.stderr)
            return 2
    except ValueError as exc:
        print(json.dumps({"error": f"Invalid JSON file format: {exc}"}), file=sys.stderr)
        return 2

    payload = {
        "contacts": contacts,
        "skipDuplicates": args.skip_duplicates,
    }

    req = Request(
        f"{base_url}/contacts/bulk-import",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )

    try:
        with urlopen(req, timeout=30) as resp:
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
