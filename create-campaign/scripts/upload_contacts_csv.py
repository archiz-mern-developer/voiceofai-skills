#!/usr/bin/env python3
"""Upload a CSV file to a VoiceOfAI campaign using multipart form-data."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main() -> int:
    parser = argparse.ArgumentParser(description="Upload CSV contacts to a campaign")
    parser.add_argument("--campaign-id", required=True, help="Campaign UUID")
    parser.add_argument("--csv-path", required=True, help="Path to CSV file")
    args = parser.parse_args()

    api_key = os.environ.get("VOICEOFAI_API_KEY")
    base_url = os.environ.get("VOICEOFAI_BASE_URL", "https://voice.voiceofai.co.in/api/v1").rstrip("/")

    if not api_key:
        print(json.dumps({"error": "VOICEOFAI_API_KEY environment variable is not set."}), file=sys.stderr)
        return 2

    csv_file = Path(args.csv_path)
    if not csv_file.exists():
        print(json.dumps({"error": f"CSV file not found: {args.csv_path}"}), file=sys.stderr)
        return 2

    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    csv_bytes = csv_file.read_bytes()

    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{csv_file.name}"\r\n'
        f"Content-Type: text/csv\r\n\r\n"
    ).encode("utf-8") + csv_bytes + f"\r\n--{boundary}--\r\n".encode("utf-8")

    req = Request(
        f"{base_url}/campaigns/{args.campaign_id}/contacts-upload",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
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
