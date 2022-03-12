# Dependancy Injections in FastAPI
#   Using dependency on whole application 
#       -> dependency is applied to every endpoint in your API!
# uvicorn ch05_routerDi_01:app
# http -v GET http://localhost:8000/router/route1 Secret-Header:"SECRET_VALUE"  -> 200 Ok
# http -v GET http://localhost:8000/router/route1 Secret-Header:"NONE"          -> 403 Forbidden
# http -v GET http://localhost:8000/router/route2 Secret-Header:"SECRET_VALUE"  -> 200 Ok
# http -v GET http://localhost:8000/router/route2 Secret-Header:"NONE"          -> 403 Forbidden
#
from typing import Optional
from fastapi import FastAPI, Depends, Header, HTTPException, status

def secret_header(secret_header: Optional[str] = Header(None)) -> None:
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)

app = FastAPI(dependencies=[Depends(secret_header)])            # -> Using dependency on whole application

@app.get("/route1")
async def route1():
    return {"route": "route1"}

@app.get("/route2")
async def route2():
    return {"route": "route2"}