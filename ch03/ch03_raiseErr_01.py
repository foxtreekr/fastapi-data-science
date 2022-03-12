# Raising HTTP errors - simple string
# uvicorn ch03_raiseErr_01:app
# http -v POST http://localhost:8000/password password="aa" password_confirm="bb"                             
from fastapi import FastAPI, Body, HTTPException, status

app = FastAPI()

@app.post("/password")
async def check_password(password: str = Body(...), password_confirm: str = Body(...)):
    if password != password_confirm:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail="Passwords don't match.",
        )
    return {"message": "Passwords match."}
