from dataclasses import dataclass, field
from typing import Optional, List
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
    body: Optional[str] = None
    state: str = 'open'
    created_at: datetime
    updated_at: datetime
    user: User
    assignees: List[User] = field(default_factory=list)
    labels: List[str] = field(default_factory=list)
    comments: int = 0

def parse_issue_from_github_event(data: dict) -> Issue:
    user_data = data['issue']['user']
    user = User(id=user_data['id'], username=user_data['login'])
    assignees = [User(id=assignee['id'], username=assignee['login']) for assignee in data['issue'].get('assignees', [])]
    labels = [label['name'] for label in data['issue'].get('labels', [])]

    issue = Issue(
        id=data['issue']['id'],
        title=data['issue']['title'],
        body=data['issue'].get('body'),
        state=data['issue']['state'],
        created_at=datetime.fromisoformat(data['issue']['created_at'].rstrip('Z')),
        updated_at=datetime.fromisoformat(data['issue']['updated_at'].rstrip('Z')),
        user=user,
        assignees=assignees,
        labels=labels,
        comments=data['issue']['comments']
    )
    return issue
