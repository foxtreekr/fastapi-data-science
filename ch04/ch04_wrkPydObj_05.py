# Pydantic Data Models
#   Working with Pydantic objects
#   1. Converting an object into a dictionary
#   2. include and exclude arguments expect a set with keys of the field you want to include or exclude 
#   3. Creating an instance from a sub-class object
#   4. Updating an instance with a partial one 
#
from typing import Dict, Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str

class PostPartialUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

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


@app.patch("/posts/{id}", response_model=PostPublic)
async def partial_update(id: int, post_update: PostPartialUpdate):
    try:
        post_db = db.posts[id]

        updated_fields = post_update.dict(exclude_unset=True)
        updated_post = post_db.copy(update=updated_fields)

        db.posts[id] = updated_post
        return updated_post
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)