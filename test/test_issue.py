import unittest
from datetime import datetime, timezone

# Assuming the parse_issue function, Issue, and User classes are defined in issue.py
from cultivator.models.issue import parse_issue, Issue, User


class TestParseIssue(unittest.TestCase):
    def setUp(self) -> None:
        self.basic_issue_json = {
            "issue": {
                "id": 1,
                "title": "Test Issue",
                "body": "This is a test issue",
                "state": "open",
                "created_at": "2024-02-10T21:23:24Z",
                "updated_at": "2024-02-10T21:23:24Z",
                "user": {
                    "id": 100,
                    "login": "user1",
                },
                "comments": 0,
                "assignees": [],
                "labels": [],
            }
        }

    def test_basic_issue(self) -> None:
        issue = parse_issue(self.basic_issue_json)
        expected_created_at = datetime.fromisoformat("2024-02-10T21:23:24").replace(
            tzinfo=timezone.utc
        )
        expected_updated_at = datetime.fromisoformat("2024-02-10T21:23:24").replace(
            tzinfo=timezone.utc
        )
        self.assertEqual(issue.id, 1)
        self.assertEqual(issue.title, "Test Issue")
        self.assertEqual(issue.state, "open")
        self.assertEqual(issue.created_at, expected_created_at)
        self.assertEqual(issue.updated_at, expected_updated_at)
        self.assertEqual(issue.user.id, 100)
        self.assertEqual(issue.user.username, "user1")
        self.assertEqual(issue.comments, 0)
        self.assertEqual(len(issue.assignees), 0)
        self.assertEqual(len(issue.labels), 0)

    def test_issue_with_optional_fields(self) -> None:
        self.basic_issue_json["issue"]["body"] = "This is a test issue"
        self.basic_issue_json["issue"]["assignees"] = [{"id": 101, "login": "user2"}]
        self.basic_issue_json["issue"]["labels"] = [{"name": "bug"}]

        issue = parse_issue(self.basic_issue_json)
        self.assertEqual(issue.body, "This is a test issue")
        self.assertEqual(len(issue.assignees), 1)
        self.assertEqual(issue.assignees[0].id, 101)
        self.assertEqual(issue.assignees[0].username, "user2")
        self.assertEqual(len(issue.labels), 1)
        self.assertEqual(issue.labels[0], "bug")

    def test_issue_without_body(self) -> None:
        del self.basic_issue_json["issue"]["body"]
        issue = parse_issue(self.basic_issue_json)
        self.assertIsNone(issue.body)


if __name__ == "__main__":
    unittest.main()
