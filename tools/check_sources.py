#!/usr/bin/env python3
"""Check official security-report landing pages for next-edition markers.

This script intentionally does not scrape or summarize report bodies.
Network/bot failures are recorded, not treated as CI failures.
"""

from __future__ import annotations

import argparse
import json
import re
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


USER_AGENT = (
    "Mozilla/5.0 (compatible; security-landscape-source-monitor/1.0; "
    "+https://github.com/moruku36/security-landscape-2026)"
)


def fetch(url: str, timeout: int = 25) -> tuple[int | None, str, str | None]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(
            request, timeout=timeout, context=ssl.create_default_context()
        ) as response:
            raw = response.read(3_000_000)
            charset = response.headers.get_content_charset() or "utf-8"
            return response.status, raw.decode(charset, errors="replace"), None
    except urllib.error.HTTPError as exc:
        return exc.code, "", f"HTTP {exc.code}"
    except Exception as exc:  # monitor should report, not crash on one source
        return None, "", f"{type(exc).__name__}: {exc}"


def matches(text: str, patterns: list[str]) -> list[str]:
    found = []
    for pattern in patterns:
        try:
            if re.search(pattern, text, re.IGNORECASE):
                found.append(pattern)
        except re.error:
            if pattern.lower() in text.lower():
                found.append(pattern)
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    registry = json.loads(Path(args.registry).read_text(encoding="utf-8"))
    results = []
    alerts = []

    for source in registry["sources"]:
        status, body, error = fetch(source["url"])
        hit = matches(body, source.get("next_patterns", [])) if body else []
        result = {
            "id": source["id"],
            "name": source["name"],
            "url": source["url"],
            "current": source["current"],
            "http_status": status,
            "error": error,
            "next_markers_found": hit,
        }
        results.append(result)
        if hit:
            alerts.append(result)

    report = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "alerts": alerts,
        "results": results,
    }
    Path(args.output).write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(json.dumps({"alerts": len(alerts), "sources": len(results)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
