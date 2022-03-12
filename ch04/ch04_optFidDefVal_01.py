# Pydantic Data Models
#   Optional fields default values 
#
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

class UserProfile(BaseModel):
    nickname: str
    location: Optional[str] = None  # -> python 3.6 이상
    #location: str | None = None    # -> python 3.10 이상
    subscribed_newsletter: bool = True
    
user = UserProfile(nickname="jdoe")
print(user)  # nickname='jdoe' location=None subscribed_newsletter=True
