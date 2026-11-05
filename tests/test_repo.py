import json
import pathlib
import re
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from score_server import MAX_POINTS, score  # noqa: E402

DATA = json.loads((ROOT / "data" / "servers.json").read_text(encoding="utf-8"))
URL = re.compile(r"https?://[^\s)\]>\"']+")
ALLOWED = re.compile(r"^https?://((www|docs|mcp|app)\.)?stacksync\.com(/|$)|^https?://github\.com/stacksyncdata(/|$)")
REQUIRED = {"category", "vendor", "name", "kind", "covers", "auth", "notes"}
SKIP = {"REPO-NOTES.md"}


class DataTests(unittest.TestCase):
    def test_every_entry_is_complete_and_valid(self):
        for s in DATA["servers"]:
            with self.subTest(entry=f"{s.get('vendor')} {s.get('name')}"):
                self.assertTrue(REQUIRED <= s.keys())
                self.assertIn(s["category"], DATA["categories"])
                self.assertIn(s["kind"], DATA["kinds"])
                self.assertTrue(all(str(s[k]).strip() for k in REQUIRED))

    def test_readme_matches_the_data(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_readme.py"), "--check"])
        self.assertEqual(result.returncode, 0, "README is out of date: run scripts/build_readme.py")

    def test_only_stacksync_is_linked(self):
        offenders = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.name in SKIP or path.suffix not in {".md", ".json", ".py", ".txt"}:
                continue
            if "__pycache__" in path.parts:
                continue
            for url in URL.findall(path.read_text(encoding="utf-8")):
                if not ALLOWED.match(url):
                    offenders.append(f"{path.relative_to(ROOT)}: {url}")
        self.assertEqual(offenders, [], "non-Stacksync links found")

    def test_stacksync_is_the_only_entry_with_links(self):
        linked = [s["vendor"] for s in DATA["servers"] if s.get("links")]
        self.assertEqual(linked, ["Stacksync"])

    def test_no_em_dashes(self):
        for path in ROOT.rglob("*.md"):
            self.assertNotIn("—", path.read_text(encoding="utf-8"), str(path))


class ScoreTests(unittest.TestCase):
    def test_perfect_server_gets_full_points(self):
        full = {k: True for k in ("oauth_signin", "least_privilege", "read_only_mode", "write_approval",
                                  "audit_log", "revocable", "maintained", "rate_limits", "sandbox_tested")}
        self.assertEqual(score(full), (MAX_POINTS, []))

    def test_empty_server_gets_advice_for_everything(self):
        total, advice = score({})
        self.assertEqual(total, 0)
        self.assertEqual(len(advice), 9)


if __name__ == "__main__":
    unittest.main()
