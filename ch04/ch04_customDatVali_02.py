# Pydantic Data Models
#   Adding custom data validation with Pydantic
#   2. Apply validation at a object level
#
#   datetime.datetime.strptime('1800-01-01', '%Y-%m-%d').date() # -> datetime.date
#   datetime.datetime.strptime('1800-01-01', '%Y-%m-%d') # -> datetime.datetime
#
from datetime import date
from pydantic import BaseModel, EmailStr, ValidationError, root_validator

class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str

    @root_validator()                           # object level validation decorator 
    def passwords_match(cls, values):           # values -> dictionary containing class all field 
        password = values.get("password")
        password_confirmation = values.get("password_confirmation")
        if password != password_confirmation:
            raise ValueError("Passwords don't match")
        return values

# Passwords not matching
try:
    UserRegistration(
        email="jdoe@example.com", password="aa", password_confirmation="bb"
    )
except ValidationError as e:
    print(str(e))

# Valid
user_registration = UserRegistration(
    email="jdoe@example.com", password="aa", password_confirmation="aa"
)
# email='jdoe@example.com' password='aa' password_confirmation='aa'
print(user_registration)
