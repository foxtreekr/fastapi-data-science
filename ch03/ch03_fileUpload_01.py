# File Upload from form(메모리 상주크기(bytes) 정도만 업로드 가능 대용량은 불가)
# uvicorn ch03_fileUpload_01:app
# $http -v --form POST http://localhost:8000/files file@./files/login.js
from fastapi import FastAPI, File

app = FastAPI()

@app.post("/files")
async def upload_file(file: bytes = File(...)):
    return {"file_size": len(file)}