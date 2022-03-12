# Dependancy Injections in FastAPI
#   Creating and using a function dependency
#
# uvicorn ch05_fncDi_01:app
# http -v GET "http://localhost:8000/items?limit=5&skip=7"
#
from typing import Tuple
from fastapi import FastAPI, Depends

app = FastAPI()

async def pagination(skip: int = 0, limit: int = 10) -> Tuple[int, int]:  # dependency definition
    return (skip, limit)

@app.get("/items")
async def list_items(p: Tuple[int, int] = Depends(pagination)): # Path operation function with dependency
    skip, limit = p
    return {"skip": skip, "limit": limit}

@app.get("/things")
async def list_things(p: Tuple[int, int] = Depends(pagination)): # Path operation function with dependency
    skip, limit = p
    return {"skip": skip, "limit": limit}