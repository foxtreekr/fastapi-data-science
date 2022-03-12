# Building a custome response -> https://www.starlette.io/responses/
#   RedirectResponse
# uvicorn ch03_custResp_03:app
# http -v --follow --all GET http://localhost:8000/redirect
#                           
from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse

app = FastAPI()

@app.get("/redirect")
async def redirect():
    return RedirectResponse("/new-url", status_code=status.HTTP_301_MOVED_PERMANENTLY)

@app.get("/new-url", response_class=PlainTextResponse)
async def text():
    return "Hello world! - from new-url"