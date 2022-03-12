# 입력제한
# uvicorn ch03_path_03:app
# http http://localhost:8000/get/admin/1
#
from enum import Enum
from fastapi import FastAPI, Path

class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"

app = FastAPI()

@app.get("/users/{type}/{id}")
async def get_user(type: UserType, id: int):
    return{"type": type, "id": id}

