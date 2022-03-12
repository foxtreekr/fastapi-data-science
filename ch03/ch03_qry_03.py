# 쿼리파라메터 숫자 입력제한 걸기
# uvicorn ch03_qry_01-1:app
# http "http://localhost:8000/users?page=5&size=50"
#
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/users")
async def get_users(page: int = Query(1, gt=0), size: int = Query(10, ge=0, le=100)):
    return {"page": page, "size": size}