from fastapi import APIRouter, Depends, status, BackgroundTasks, Response
from fastapi.security import OAuth2PasswordRequestForm
from typing import Dict, List, Optional

from src.schemas.authentication import SignupIn, TokenOut

from src.utils.authentication import create_access_token, verify_password, generate_token, is_expired_token
from src.utils.exceptions import raise_credentials_exception, raise_expired_token_exception, raise_not_activated_exception, raise_user_already_exist_exception
from src.utils.send_mail import send_activation_mail

from src.queries.user import find_user_by_email_or_username, find_user_by_token, verify_user, register_user

auth_router = APIRouter(prefix="/api/v1/authentication", tags=["Authentication"])
    

@auth_router.post("/login", response_model=TokenOut, status_code=status.HTTP_200_OK)
async def login_api(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login for token
    """
    current_user = await find_user_by_email_or_username(form_data.username, form_data.username)
    if current_user and verify_password(form_data.password, current_user['hashed_password']) and current_user['is_verified']:
        return create_access_token(current_user['username'], current_user['pk'])
    if current_user and verify_password(form_data.password, current_user['hashed_password']) and not current_user['is_verified']:
        raise_not_activated_exception()
    raise_credentials_exception()


@auth_router.post("/activate-account/{token}", status_code=status.HTTP_204_NO_CONTENT)
async def activate_account_api(token: str):
    """
    Forgot password
    """
    current_user = await find_user_by_token(token)
    if current_user and is_expired_token(current_user['token_expired_at']):
        await verify_user(current_user['pk'])
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise_expired_token_exception()


@auth_router.post("/signup", status_code=status.HTTP_204_NO_CONTENT)
async def signup_api(obj: SignupIn, background_tasks: BackgroundTasks):
    """
    Signup
    """
    user = await find_user_by_email_or_username(obj.email, obj.username)
    if user:
        raise_user_already_exist_exception()
    values = obj.dict()
    values['token'], values['token_expired_at'] = generate_token()
    await register_user(values)
    background_tasks.add_task(send_activation_mail, values['first_name'], values['email'], values['token'])
    print("token is", values['token'])
    return Response(status_code=status.HTTP_204_NO_CONTENT)
