# Building a custome response -> https://www.starlette.io/responses/
#   -- StreamingResponse
#   Custom response
# uvicorn ch03_custResp_05:app
# http -v GET http://localhost:8000/xml
#                           
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/xml")
async def get_xml():
    content = """<?xml version="1.0" encoding="UTF-8"?>
        <Hello>World</Hello>
    """
    return Response(content=content, media_type="application/xml")
