# Building a custome response -> https://www.starlette.io/responses/
#   HTMLResponse
#   PlainTextResponse
# uvicorn ch03_custResp_01:app
# http -v GET http://localhost:8000/html
# http -v GET http://localhost:8000/hext
#                           
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse

app = FastAPI()


@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return """
        <html>
            <head>
                <title>Hello world!</title>
            </head>
            <body>
                <h1>Hello world!</h1>
            </body>
        </html>
    """


@app.get("/text", response_class=PlainTextResponse)
async def text():
    return "Hello world!"