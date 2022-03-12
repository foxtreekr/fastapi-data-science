from typing import Dict

from ch03Proj.models.user import User
from ch03Proj.models.post import Post


class DummyDatabase:
    users: Dict[int, User] = {}
    posts: Dict[int, Post] = {}


db = DummyDatabase()
