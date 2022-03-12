# The Response Path Parameter
# uvicorn ch03_respPathPar_03:app
# $http -v GET http://localhost:8000/posts/1
from fastapi import FastAPI, status
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