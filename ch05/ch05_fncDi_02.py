# Dependancy Injections in FastAPI
#   Creating and using a  more complex function dependency
#
# uvicorn ch05_fncDi_02:app
# http -v GET "http://localhost:8000/items?limit=-15&skip=7"
# http -v GET "http://localhost:8000/items?limit=120&skip=7"
#
from typing import Tuple
from fastapi import FastAPI, Depends, Query

app = FastAPI()

async def pagination(
    skip: int = Query(0, ge=0),         # Query function to our argument to add a validation constraint => validation fault is error 422 raise 
    limit: int = Query(10, ge=0),
) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)

@app.get("/items")
async def list_items(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}

@app.get("/things")
async def list_things(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


