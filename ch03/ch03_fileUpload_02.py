# File Upload from form(대용량 업로드, 메모리 한계까지 업로드 및 초과시 디스크의 임시위치에 저장, 메모리 부족없이 대용량 파일 접근가능)
# uvicorn ch03_fileUpload_02:app
# $http -v --form POST http://localhost:8000/files file@./files/login.js
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files")
async def upload_file(file: UploadFile = File(...)):
    return {"file_name": file.filename, "content_type": file.content_type}