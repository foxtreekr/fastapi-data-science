# 쿼리파라메터 사용
# uvicorn ch03_qry_01:app
# http "http://localhost:8000/users?page=5&size=50"
#
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users")
async def get_users(page: int = 1, size: int = 10):
    return {"page": page, "size": size}