# The Response Path Parameter nb_views를 노출되지 않도록 모델을 새로 만들고 respose_model로 지정 마치 database의 view와 비슷
# uvicorn ch03_respPathPar_04:app
# $http -v GET http://localhost:8000/posts/1
from fastapi import FastAPI, status
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    nb_views: int

class PublicPost(BaseModel):
    title: str

# Dummy database
posts = { 
    1: Post(title="Helllo", nb_views=100)
}

app = FastAPI()

@app.get("/posts/{id}", response_model=PublicPost)
async def get_post(id: int):
    return posts[id]
