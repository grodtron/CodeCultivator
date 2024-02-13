from dataclasses import dataclass, field
from typing import Optional, List, Dict
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

def parse_issue(data: Dict[str, any]) -> Issue:
    user_data = data['issue']['user']
    user = User(id=user_data['id'], username=user_data['login'])
    assignees = [User(id=assignee['id'], username=assignee['login']) for assignee in data['issue'].get('assignees', [])]
    labels = [label for label in data['issue'].get('labels', [])]

    issue = Issue(
        id=data['issue']['id'],
        title=data['issue']['title'],
        state=data['issue']['state'],
        created_at=datetime.fromisoformat(data['issue']['created_at'].rstrip('Z')),
        updated_at=datetime.fromisoformat(data['issue']['updated_at'].rstrip('Z')),
        user=user,
        body=data['issue'].get('body'),
        comments=data['issue']['comments'],
        assignees=assignees,
        labels=labels
    )
    return issue
