# Header & Coookies
# uvicorn ch03_headers_cookies_03:app
# $http -v http://localhost:8000 Cookie:hello=foo
from typing import Optional
from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get("/")
#async def get_cookie(hello: Optional[str] = Cookie(None)):
#    return {"hello": hello}
async def get_cookie(hello: str = Cookie(...)):
    return {"hello": hello}