import unittest
from lint import lint


class IntentLinterTests(unittest.TestCase):
    def test_rejects_docs_commit_with_code(self):
        report = lint({"subject": "docs: update", "files": ["src/app.py"]})
        self.assertIn("docs-contains-code", report["issues"])

    def test_requires_tests_for_fix(self):
        report = lint({"subject": "fix: timeout", "files": ["src/net.py"], "tests": False})
        self.assertIn("change-without-tests", report["issues"])

    def test_requires_breaking_marker(self):
        report = lint({"subject": "feat: api", "files": ["api.py"], "tests": True, "breaking_api": True})
        self.assertIn("breaking-change-not-marked", report["issues"])


if __name__ == "__main__":
    unittest.main()
