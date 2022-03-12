# Dependancy Injections in FastAPI
#   Using dependency on whole router
#       app.include_router dependencies   
#           ==> recommend APIRouter dependencies   
# uvicorn ch05_routerDi_01:app
# http -v GET http://localhost:8000/router/route1 Secret-Header:"SECRET_VALUE"  -> 200 Ok
# http -v GET http://localhost:8000/router/route1 Secret-Header:"NONE"          -> 403 Forbidden
# http -v GET http://localhost:8000/router/route2 Secret-Header:"SECRET_VALUE"  -> 200 Ok
# http -v GET http://localhost:8000/router/route2 Secret-Header:"NONE"          -> 403 Forbidden
#
from typing import Optional
from fastapi import APIRouter, FastAPI, Depends, Header, HTTPException, status

def secret_header(secret_header: Optional[str] = Header(None)) -> None:
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)

router = APIRouter()

@router.get("/route1")
async def router_route1():
    return {"route": "route1"}

@router.get("/route2")
async def router_route2():
    return {"route": "route2"}

app = FastAPI()
app.include_router(router, prefix="/router", dependencies=[Depends(secret_header)])
