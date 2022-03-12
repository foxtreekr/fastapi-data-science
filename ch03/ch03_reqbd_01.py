# body 요구(POST)
# uvicorn ch03_reqbd_01:app
# http -v POST http://localhost:8000/users name="John" age=30
#
from fastapi import FastAPI, Path, Query, Body 

app = FastAPI()

@app.post("/users")
async def create_users(name: str = Body(...), age: int = Body(...)):
    return {"name": name, "age": age}