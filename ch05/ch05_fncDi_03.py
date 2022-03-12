# Dependancy Injections in FastAPI
#   Get an Object or raise a 404 error
#
# uvicorn ch05_fncDi_03:app
# http -v GET "http://localhost:8000/posts/1"                           => 200 Ok
# http -v GET "http://localhost:8000/posts/5"                           => 404 Error
# http -v DELETE "http://localhost:8000/posts/1"                        => 204 No Content 
# http -v DELETE "http://localhost:8000/posts/1"                        => 404 Error
# http -v PATCH http://localhost:8000/posts/2 title="Updated title"     => 200 Ok
# http -v PATCH http://localhost:8000/posts/1 title="Updated title"    => 404 Error
#
from typing import Dict, Optional
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel

class Post(BaseModel):
    id: int
    title: str
    content: str

class PostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]

class DummyDatabase:
    posts: Dict[int, Post] = {}

db = DummyDatabase()
db.posts = {
    1: Post(id=1, title="Post 1", content="Content 1"),
    2: Post(id=2, title="Post 2", content="Content 2"),
    3: Post(id=3, title="Post 3", content="Content 3"),
}

app = FastAPI()

async def get_post_or_404(id: int) -> Post:
    try:
        return db.posts[id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.get("/posts/{id}")
async def get(post: Post = Depends(get_post_or_404)):
    return post

@app.patch("/posts/{id}")
async def update(post_update: PostUpdate, post: Post = Depends(get_post_or_404)):
    updated_post = post.copy(update=post_update.dict())
    db.posts[post.id] = updated_post
    return updated_post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(post: Post = Depends(get_post_or_404)):
    db.posts.pop(post.id)