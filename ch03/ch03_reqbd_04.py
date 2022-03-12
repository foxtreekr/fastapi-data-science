# body 요구(POST JSON) 및 priority 값의 제한
# uvicorn ch03_reqbd_02:app
# $echo '{"user":{"name":"John", "age":30}, "priority":1}'| http -v -j POST http://localhost:8000/users

from fastapi import FastAPI, Body
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class Company(BaseModel):
    name: str

app = FastAPI()

@app.post("/users")
async def create_user(user: User, priority: int = Body(..., ge=1, le=3)):
    return {"user": user, "priority": priority}