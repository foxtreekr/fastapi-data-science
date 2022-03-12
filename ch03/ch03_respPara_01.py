# The Response parameter  1. Custom-Header
# uvicorn ch03_respPar_01:app
# $http -v GET http://localhost:8000
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def custom_header(response: Response):
    response.headers["Custom-Header"] = "Custom-Header-Value" # dynamically response parameter
    response.headers["Custom-No"] = "3939" # dynamically response parameter
    return {"hello": "world"}
