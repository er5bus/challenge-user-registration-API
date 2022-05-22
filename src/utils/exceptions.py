from fastapi import HTTPException, status


class BaseHTTPException(Exception):
    def __init__(self, status_code: int = status.HTTP_400_BAD_REQUEST, error_code: str = 100, error_message: str = 'something wrong happens'):
        self.status_code = status_code
        self.error_code = error_code
        self.error_message = error_message

    def to_dict(self):
        return dict(status_code=self.status_code, error_code=self.error_code, error_message=self.error_message)


def raise_credentials_exception(reason: str = "Could not validate credentials"):
    raise BaseHTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        error_code=100,
        error_message=reason
    )


def raise_expired_token_exception(reason: str = "Your token either expired or not exists"):
    raise BaseHTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        error_code=101,
        error_message=reason
    )


def raise_not_activated_exception(reason: str = "This user need activation"):
    raise BaseHTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        error_code=102,
        error_message=reason
    )


def raise_user_already_exist_exception(reason: str = "User already exists"):
    raise BaseHTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        error_code=103,
        error_message=reason
    )

