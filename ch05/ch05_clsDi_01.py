# Dependancy Injections in FastAPI
#   Creating and using a parameterized dependency with a class
#
# uvicorn ch05_clsDi_01:app
# http -v GET "http://localhost:8000/items?limit=-15&skip=7"
# http -v GET "http://localhost:8000/items?limit=120&skip=7"
#
from typing import Tuple
from fastapi import FastAPI, Depends, Query

app = FastAPI()

class Pagination:
    def __init__(self, maximum_limit: int = 100):   # 생성자
        self.maximum_limit = maximum_limit

    async def __call__(                             # 인스턴스 호출(function call)
        self,
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=0),
    ) -> Tuple[int, int]:
        capped_limit = min(self.maximum_limit, limit)
        return (skip, capped_limit)

pagination = Pagination(maximum_limit=50)

@app.get("/items")
async def list_items(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}

@app.get("/things")
async def list_things(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}