# body 요구(POST)
# 1개의 객체
# uvicorn ch03_reqbd_02:app
# $ http -v -j POST http://localhost:8000/users name="john", age=10

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel 

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/users")
async def create_users(user: User):
    return user