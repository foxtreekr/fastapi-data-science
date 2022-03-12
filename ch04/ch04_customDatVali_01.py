# Pydantic Data Models
#   Adding custom data validation with Pydantic
#   1. Apply validation at a field level
#
#   datetime.datetime.strptime('1800-01-01', '%Y-%m-%d').date() # -> datetime.date
#   datetime.datetime.strptime('1800-01-01', '%Y-%m-%d') # -> datetime.datetime
#
from datetime import date
from pydantic import BaseModel, ValidationError, validator

class Person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

    @validator("birthdate")
    def valid_birthdate(cls, v: date):              # static class method first argument cls being the class itself
        delta = date.today() - v                    # delta -> datetime.timedelta(days=81152)
        age = delta.days / 365
        if age > 120:
            raise ValueError("You seem a bit too old!")
        return "foo"


# Invalid birthdate
try:
    Person(first_name="John", last_name="Doe", birthdate="1800-01-01")
except ValidationError as e:
    print(str(e))

# Valid
person = Person(first_name="John", last_name="Doe", birthdate="1991-01-01")
print(person)  # first_name='John' last_name='Doe' birthdate='foo'
