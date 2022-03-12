# Pydantic Data Models
#   fields validation - Dynamic default values => default_factory 객체 생성시 적용
#
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

def list_factory():  # --> 단순값이 아닐경우 함수를 만들어서 값을 전달해야 한다.
    return ["a", "b", "c"]

class Model(BaseModel):
    l: List[str] = Field(default_factory=list_factory)
    d: datetime = Field(default_factory=datetime.now)
    l2: List[str] = Field(default_factory=list)

o1 = Model()
print(o1.l)  # ["a", "b", "c"]
print(o1.l2)  # []

o1.l.append("d")
print(o1.l, o1.d)  # ["a", "b", "c", "d"]

o2 = Model()
print(o2.l)  # ["a", "b", "c"]
print(o2.l2)  # []
print(o2.l, o2.d)

print(o1.d < o2.d)  # True