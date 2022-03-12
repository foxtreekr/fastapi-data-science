# The Response Path Parameter
# uvicorn ch03_respPathPar_02:app
# $http -v DELETE http://localhost:8000/posts/1
from fastapi import FastAPI, status
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    nv_views: int

# Dummy database
posts = { 
    1: Post(title="Helllo", nb_views=100)
}

app = FastAPI()

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    posts.pop(id, None)
    return None
