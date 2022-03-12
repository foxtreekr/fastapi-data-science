# Form Data post or get
# uvicorn ch03_frmdat_01:app
# $http -v --form POST http://localhost:8000/users name=John age=30
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/users")
async def create_user(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}