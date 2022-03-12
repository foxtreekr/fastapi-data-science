# Dependancy Injections in FastAPI
#   What is dependency injection?
#
# uvicorn ch05_whatIsDi_01:app
# http -v GET http://localhost:8000
#
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/")
async def header(user_agent: str = Header(...)):    # <- Dependancy Injections 
    return {"user_agent": user_agent}               # we just ask for the value we need That's dependancy injection
