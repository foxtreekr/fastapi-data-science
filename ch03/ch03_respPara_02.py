# The Response parameter  2. Cookie
# uvicorn ch03_respPar_02:app
# $http -v GET http://localhost:8000
from fastapi import FastAPI, Response


app = FastAPI()

@app.get("/")
async def custom_cookie(response: Response):
    response.set_cookie("cookie-name", "cookie-value", max_age=86400) # dynamically response parameter
    response.set_cookie("cookie-3333", "32;33;31;35", max_age=9999) # dynamically response parameter
    return {"hello": "world"}
