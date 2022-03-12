# Pydantic Data Models
#   Standard field types
#       
from pydantic import BaseModel

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int