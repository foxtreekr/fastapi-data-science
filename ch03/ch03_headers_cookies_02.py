# Header & Coookies
# uvicorn ch03_headers_cookies_02:app
# $http -v -h GET http://localhost:8000
from typing import List
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/")
async def get_header(user_agent: str = Header(...)):
    return {"user_agent": user_agent}