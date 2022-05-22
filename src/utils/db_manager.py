import databases

from src.settings.config import configurations

from .authentication import get_password_hash


async def db_upgrade():
    database_url = configurations.database_test_url if configurations.testing else configurations.database_url
    async with databases.Database(database_url) as database:
        query = """CREATE TABLE IF NOT EXISTS users
            (pk SERIAL PRIMARY KEY, first_name VARCHAR(100) NULL, is_verified BOOLEAN default False,
            last_name VARCHAR(100) NULL, username VARCHAR(50) NOT NULL UNIQUE, email VARCHAR(120) NOT NULL UNIQUE,
            token VARCHAR(4) default NULL, token_expired_at timestamp default NULL, hashed_password VARCHAR(200))"""
        await database.execute(query=query)


async def db_downgrade():
    database_url = configurations.database_test_url if configurations.testing else configurations.database_url
    async with databases.Database(database_url) as database:
        query = """DROP TABLE IF EXISTS users"""
        await database.execute(query=query)
