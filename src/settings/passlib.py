from passlib.context import CryptContext
from passlib.totp import TOTP

from .config import configurations

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
