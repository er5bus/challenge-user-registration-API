from src.settings.db import database


async def find_user_by_email_or_username(email: str, username: str):
    query = "SELECT * FROM users WHERE email = :email or username = :username"
    return await database.fetch_one(query=query, values={ 'email': email, 'username': username })

async def find_user_by_token(token:str):
    query = "SELECT * FROM users WHERE token = :token"
    return await database.fetch_one(query=query, values={ 'token': token })

async def verify_user(pk: int):
    query = "UPDATE users SET token = :token, is_verified = :is_verified, token_expired_at = :token_expired_at WHERE pk = :pk"
    return await database.execute(query=query, values={'token': None, 'is_verified': True, 'token_expired_at': None, 'pk': pk})

async def register_user(values):
    query = """INSERT INTO users
(first_name, last_name, username, email, hashed_password, token, token_expired_at)
VALUES (:first_name, :last_name, :username, :email, :hashed_password, :token, :token_expired_at)"""
    await database.execute(query=query, values=values)

