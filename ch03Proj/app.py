#
# uvicorn ch03Proj.app:app
#
from fastapi import FastAPI

from ch03Proj.routers.posts import router as posts_router
from ch03Proj.routers.users import router as users_router

app = FastAPI()

app.include_router(posts_router, prefix="/posts", tags=["posts"])
app.include_router(users_router, prefix="/users", tags=["users"])
