# Pydantic Data Models
#   Creating model variations with class inheritance
#
from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str

class PostPublic(BaseModel):
    id: int
    title: str
    content: str

class PostDB(BaseModel):
    id: int
    title: str
    content: str
    nb_views: int = 0
