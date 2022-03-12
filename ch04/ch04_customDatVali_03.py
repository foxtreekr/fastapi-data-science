# Pydantic Data Models
#   Adding custom data validation with Pydantic
#   3. Apply validation before Pydantic parsing
# 
#   @ Be default, your validator are run after Pydantic has done its parsing work
#
from typing import List
from pydantic import BaseModel, validator

class Model(BaseModel):
    values: List[int]

    @validator("values", pre=True)
    def split_string_values(cls, v):
        if isinstance(v, str):
            return v.split(",")  # -> '1,2,3'.split(',') => ['1', '2', '3']
        return v


m = Model(values="1,2,3")
print(m.values)  # [1, 2, 3]

