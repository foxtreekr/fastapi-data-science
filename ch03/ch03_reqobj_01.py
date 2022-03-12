# The request object
# uvicorn ch03_reqobj_01:app
# $http -v http://localhost:8000
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def get_request_object(request: Request):
    return {"path": request.url.path}
