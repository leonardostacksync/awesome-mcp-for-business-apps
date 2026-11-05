"""Score an MCP server against a readiness checklist before you connect it to business data.

Describe a server in a small JSON file (see examples/), then:

    python scripts/score_server.py examples/remote-oauth-readonly.json

The score is a prompt for a decision, not a verdict. Standard library only.
"""
from __future__ import annotations

import json
import sys

# criterion key -> (points, question, advice when the answer is no)
CRITERIA: dict[str, tuple[int, str, str]] = {
    "oauth_signin": (3, "Does it sign in with OAuth instead of a static key?", "Prefer OAuth. A static key in a chat or a config file is hard to revoke."),
    "least_privilege": (3, "Does it act with the signed-in person's permissions, or a narrow role?", "Give it a dedicated least-privilege role. Never a full admin."),
    "read_only_mode": (2, "Can you restrict it to read access?", "Start read-only and add writes only when needed."),
    "write_approval": (3, "Can writes require a person's approval?", "Add an approval step or a human confirmation before changes."),
    "audit_log": (2, "Can you see what it did?", "Without a log you cannot review or debug an agent's changes."),
    "revocable": (2, "Can you revoke its access immediately?", "You need a way to cut off a misbehaving client."),
    "maintained": (2, "Is it maintained, with recent releases?", "An unmaintained server is a risk. Check its recent activity."),
    "rate_limits": (1, "Are there rate limits or quotas?", "Add limits so a loop cannot exhaust an API."),
    "sandbox_tested": (1, "Have you tested it on a sandbox or copy?", "Test on non-production data first."),
}
MAX_POINTS = sum(c[0] for c in CRITERIA.values())


def score(server: dict) -> tuple[int, list[str]]:
    total = 0
    advice: list[str] = []
    for key, (points, _question, tip) in CRITERIA.items():
        if server.get(key) is True:
            total += points
        else:
            advice.append(tip)
    return total, advice


def label(total: int) -> str:
    ratio = total / MAX_POINTS
    if ratio >= 0.8:
        return "ready for a pilot on real data, with approvals"
    if ratio >= 0.5:
        return "use on a sandbox or read-only until the gaps are closed"
    return "do not connect to business data yet"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Usage: python score_server.py server.json")
    with open(sys.argv[1], encoding="utf-8") as fh:
        server = json.load(fh)
    total, advice = score(server)
    print(f"{server.get('name', 'server')}: {total}/{MAX_POINTS}, {label(total)}")
    for tip in advice:
        print(f"  - {tip}")


if __name__ == "__main__":
    main()
