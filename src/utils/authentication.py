import random

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

from datetime import datetime, timedelta
from typing import Optional, Dict, Any

from src.settings.passlib import pwd_context, configurations

from .exceptions import raise_credentials_exception


def verify_password(plain_password: str, hashed_password: str) -> str:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(username: str, pk: int) -> Dict[str, str]:
    data={"sub": username, "pk": pk}
    expires_delta=timedelta(minutes=configurations.access_token_expire_minutes)
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, configurations.secret_key, algorithm=configurations.algorithm)
    return { "access_token": encoded_jwt, "token_type": "bearer" }

def generate_token() -> str:
    ot = random.choices('1234567890', k = 4)
    return ''.join(ot), datetime.now()

def is_expired_token(date: datetime) -> str:
    return datetime.now() < (date + timedelta(seconds=configurations.activation_token_expire_seconds))

def get_payload(token: str) -> Dict[str, str]:
    try:
        return jwt.decode(token, configurations.secret_key, algorithms=[configurations.algorithm])
    except JWTError:
        raise_credentials_exception()
