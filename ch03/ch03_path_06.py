# 정규표현식
# uvicorn ch03_path_06:app
# http http://localhost:8000/license-plates/AB-123-C
#
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/license-plates/{license}")
async def get_license_plate(license: str = Path(...,regex=r"^\w{2}-\d{3}-\w{2}$")):
    return {"license": license}