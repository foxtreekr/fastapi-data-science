# Dependancy Injections in FastAPI
#   Using dependencies at a path, router, and global level
#   cf) Path Operation Decorator's Dependency
#       만약에 디펜던시가 리턴하는 값이 필요하지 않고 실행만 할경우  데코레이터 dependencies 파라미터에 Depends를 list형태로 넘겨준다.
#       ex) @app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
#
# uvicorn ch05_pathDi_01:app
# http -v GET http://localhost:8000/protected-route Secret-Header:"SECRET_VALUE"
#
from typing import Optional
from fastapi import FastAPI, Depends, Header, HTTPException, status

app = FastAPI()

def secret_header(secret_header: Optional[str] = Header(None)) -> None: 
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)

@app.get("/protected-route", dependencies=[Depends(secret_header)]) # -> Path Operation Decorator's Dependency
async def protected_route():
    return {"hello": "world"}