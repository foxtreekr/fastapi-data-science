# Pydantic Data Models
#   Optional fields default values 
#
import time
from typing import List
from datetime import datetime
from pydantic import BaseModel

class Model(BaseModel):
    # Don't do this.
    # This example shows you why it doesn't work.
    d: datetime = datetime.now()
    l: List[str] = ["a", "b", "c"] 

o1 = Model()
a = o1.l
print(o1.d, hex(id(a)), o1.l )

time.sleep(1)  # Wait for a second

o2 = Model()
b = o2.l
print(o2.d, hex(id(b)), o2.l)

print(o1.d < o2.d)  # False
print(o1.l == o2.l)  # False
