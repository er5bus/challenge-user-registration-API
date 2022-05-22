from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field, validator

from src.utils.authentication import get_password_hash

from . import BaseConfig


class SignupIn(BaseModel):
    username: str = Field(..., title='username', max_length=50)
    email: EmailStr = Field(..., title='email')
    hashed_password: str = Field(..., alias='plainPassword', min_lenght=8, max_length=50, title='password')
    last_name: str = Field(..., title='First name', description='Client last name', max_length=100)
    first_name: str = Field(..., title='Last name', description='Client first name', max_length=100)

    @validator('hashed_password')
    def password_encryption(cls, password):
        return get_password_hash(password)

    class Config(BaseConfig):
        orm_mode = True


class TokenOut(BaseModel):
    access_token: str = Field(..., title='Access token')
    token_type: str = Field(..., title='Token type')
