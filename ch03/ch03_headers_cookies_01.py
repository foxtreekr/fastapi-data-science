# Header & Coookies
# uvicorn ch03_headers_cookies_01:app
# $http -v -h GET http://localhost:8000 'Hello: World'
from typing import List
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/")
async def get_header(hello: str = Header(...)):
    return {"hello": hello}