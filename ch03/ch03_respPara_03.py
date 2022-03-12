# The Response parameter  Status code 
# uvicorn ch03_respPar_03:app
# http -v PUT http://localhost:8000/posts/2 title="Updated title" nb_views=101
# http -v GET http://localhost:8000/posts/2                                
from fastapi import FastAPI, Response, status
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    nb_views: int

# Dummy database
posts = { 
    1: Post(title="Helllo", nb_views=100)
}

app = FastAPI()

@app.get("/posts/{id}")
async def get_post(id: int):
    return posts[id]

@app.put("/posts/{id}")
async def update_or_create_post(id: int, post: Post, response: Response):
    if id not in posts:
        response.status_code = status.HTTP_201_CREATED
    posts[id] = post
    return posts[id]