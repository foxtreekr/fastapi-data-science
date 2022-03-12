# Pydantic Data Models
#   Working with Pydantic objects
#   1. Converting an object into a dictionary
#   2. include and exclude arguments expect a set with keys of the field you want to include or exclude
#   3. Creating an instance from a sub-class object
# 
from typing import Dict

from fastapi import FastAPI, status
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostPublic(PostBase):
    id: int

class PostDB(PostBase):
    id: int
    nb_views: int = 0

class DummyDatabase:
    posts: Dict[int, PostDB] = {}

db = DummyDatabase()

app = FastAPI()

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=PostPublic)
async def create(post_create: PostCreate):
    new_id = max(db.posts.keys() or (0,)) + 1

    post = PostDB(id=new_id, **post_create.dict())  # => ** in function call is to transform a dictionary such as {"title": "Foo", "content": "Bar"}
                                                    # => into keyword argumnts  suech as this title="foo", content="Bar"
    db.posts[new_id] = post
    return post