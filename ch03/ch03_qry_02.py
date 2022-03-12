# 나열형 쿼리파라메터 사용
# uvicorn ch03_qry_02:app
# http "http://localhost:8000/users?format=full"
#
from enum import Enum
from fastapi import FastAPI

class UsersFormat(str, Enum):
    SHORT = "short"
    FULL = "full"

app = FastAPI()

@app.get("/users")
async def get_users(format:  UsersFormat):
    return {"format": format}