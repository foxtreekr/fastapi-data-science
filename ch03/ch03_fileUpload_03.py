# File Upload from form(다중파일)
# uvicorn ch03_fileUpload_04:app
# $http --form POST http://localhost:8000/files files@./files/1.jpg files@./files/2.jpg files@./files/3.png
from typing import List
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    return [
        {"file_name": file.filename, "content_type": file.content_type}
        for file in files
    ]
