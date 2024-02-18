from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from datetime import datetime
import json


@dataclass
class User:
    id: int
    username: str


@dataclass
class Issue:
    id: int
    title: str
    state: str
    created_at: datetime
    updated_at: datetime
    user: User
    body: Optional[str] = None
    comments: int = 0
    assignees: List[User] = field(default_factory=list)
    labels: List[str] = field(default_factory=list)


def parse_issue(data: Dict[str, Any]) -> Issue:
    issue_data = data["issue"]
    user_data = issue_data["user"]
    user = User(id=user_data["id"], username=user_data["login"])
    assignees = [
        User(id=assignee["id"], username=assignee["login"])
        for assignee in issue_data.get("assignees", [])
    ]
    labels = [label["name"] for label in issue_data.get("labels", [])]

    issue = Issue(
        id=issue_data["id"],
        title=issue_data["title"],
        state=issue_data["state"],
        created_at=datetime.fromisoformat(issue_data["created_at"].rstrip("Z")),
        updated_at=datetime.fromisoformat(issue_data["updated_at"].rstrip("Z")),
        user=user,
        body=issue_data.get("body"),
        comments=issue_data["comments"],
        assignees=assignees,
        labels=labels,
    )
    return issue
