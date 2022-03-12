# body 요구(POST)
# uvicorn ch03_reqbd_02:app
# $echo '{"user":{"name":"John", "age":30}, "company":{"name": "ACME"}}'| http -v -j POST http://localhost:8000/users
# Bash only ->
# $http -v -j POST http://localhost:8000/users user[name]='pie' user[age]=10 company[name]='ACME'


from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class Company(BaseModel):
    name: str

app = FastAPI()

@app.post("/users")
async def create_user(user: User, company: Company):
    return {"user": user, "company": company}