# 사용자 id제한 1보다 클것
# uvicorn ch03_path_04:app
# http http://localhost:8000/users/1
#
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{id}")
async def get_user(id: int = Path(...,title="msg" ,ge=1)):
    return {"id": id}