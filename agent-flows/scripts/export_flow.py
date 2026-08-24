#!/usr/bin/env python3
"""Export flow graph from a visual flow agent."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main() -> int:
    parser = argparse.ArgumentParser(description="Export flow graph for a flow-type agent")
    parser.add_argument("--agent-id", required=True, help="Flow agent UUID")
    parser.add_argument("--output", help="Optional output JSON file path")
    args = parser.parse_args()

    api_key = os.environ.get("VOICEOFAI_API_KEY")
    base_url = os.environ.get("VOICEOFAI_BASE_URL", "https://voice.voiceofai.co.in/api/v1").rstrip("/")

    if not api_key:
        print(json.dumps({"error": "VOICEOFAI_API_KEY environment variable is not set."}), file=sys.stderr)
        return 2

    req = Request(
        f"{base_url}/agents/{args.agent_id}/flow",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        },
        method="GET",
    )

    try:
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            formatted = json.dumps(data, indent=2)

            if args.output:
                out_path = Path(args.output)
                out_path.write_text(formatted, encoding="utf-8")
                print(json.dumps({"status": "exported", "file": str(out_path)}, indent=2))
            else:
                print(formatted)
            return 0
    except HTTPError as exc:
        print(json.dumps({"status_code": exc.code, "error": exc.read().decode("utf-8")}, indent=2), file=sys.stderr)
        return 1
    except URLError as exc:
        print(json.dumps({"error": str(exc.reason)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
