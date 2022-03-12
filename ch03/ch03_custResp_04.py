# Building a custome response -> https://www.starlette.io/responses/
#   FileResponse
# pip3 install aiofiles
# uvicorn ch03_custResp_04:app
# http -v GET http://localhost:8000/cat
#
# __file__ 을 파이썬 인터프리터에서 실행시 아래의 코드를 실행하여 __file__을 대치해줘야 함
# print(os.getcwd())
# print(sys.argv[0])
# print(os.path.dirname(os.path.realpath('__file__')))
#
from os import path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/cat")
async def get_cat():
    root_directory = path.dirname(path.dirname(__file__))
    picture_path = path.join(root_directory, "assets", "cat.jpg")
    return FileResponse(picture_path)