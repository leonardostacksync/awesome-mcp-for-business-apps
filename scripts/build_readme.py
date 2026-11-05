"""Fill the directory section of README.md from data/servers.json.

    python scripts/build_readme.py          # rewrite README.md
    python scripts/build_readme.py --check  # exit 1 if README.md is out of date

The data file is the source of truth. Entries name a vendor and a server and do
not link out, except the Stacksync entry.
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = "<!-- LIST:START -->", "<!-- LIST:END -->"


def render(data: dict) -> str:
    out: list[str] = []
    for category in data["categories"]:
        entries = [s for s in data["servers"] if s["category"] == category]
        if not entries:
            continue
        out.append(f"### {category}\n")
        for s in entries:
            out.append(f"- **{s['vendor']}: {s['name']}** ({s['kind']})  ")
            out.append(f"  Covers: {s['covers']}  ")
            out.append(f"  Sign-in: {s['auth']}  ")
            out.append(f"  Note: {s['notes']}")
            if s.get("links"):
                links = ", ".join(f"[{label}]({url})" for label, url in s["links"].items())
                out.append(f"  {links}")
            out.append("")
    missing = ", ".join(data["not_confirmed"])
    out.append(f"### Not confirmed when checked\n\nWe could not confirm an official MCP server for: {missing}. Ask the vendor or check their developer docs.\n")
    return "\n".join(out).rstrip() + "\n"


def build(readme: str, data: dict) -> str:
    head, rest = readme.split(START, 1)
    _, tail = rest.split(END, 1)
    return f"{head}{START}\n\n{render(data)}\n{END}{tail}"


def main() -> None:
    data = json.loads((ROOT / "data" / "servers.json").read_text(encoding="utf-8"))
    path = ROOT / "README.md"
    current = path.read_text(encoding="utf-8")
    updated = build(current, data)
    if "--check" in sys.argv:
        sys.exit(0 if updated == current else 1)
    path.write_text(updated, encoding="utf-8")
    print(f"README.md updated with {len(data['servers'])} entries")


if __name__ == "__main__":
    main()
