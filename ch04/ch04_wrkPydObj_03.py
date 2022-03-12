# Pydantic Data Models
#   Working with Pydantic objects
#   1. Converting an object into a dictionary
#   2. include and exclude arguments expect a set with keys of the field you want to include or exclude
# 
# class Signal(str, Enum):
#     red = 'red'
#     green = 'green'
#     orange = 'orange'
# 
# brain_detected_colour = 'red'
# brain_detected_colour == Signal.red  # direct comparison
# 
from datetime import date
from enum import Enum
from typing import List

from pydantic import BaseModel


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"


class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]
    address: Address

    def name_dict(self):
        return self.dict(include={"first_name", "last_name"})


person = Person(
    first_name="John",
    last_name="Doe",
    gender=Gender.MALE,
    birthdate="1991-01-01",
    interests=["travel", "sports"],
    address={
        "street_address": "12 Squirell Street",
        "postal_code": "424242",
        "city": "Woodtown",
        "country": "US",
    },
)

name_dict = person.name_dict()
print(name_dict)  # {"first_name": "John", "last_name": "Doe"}