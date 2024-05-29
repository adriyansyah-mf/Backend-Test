from api.config import cfg
from core.db import engine
from models.admin import AdminModel
from helpers.authentication import PasswordHasher, BasicSalt
import asyncio

async def main():
    async with engine.begin() as conn:
        hasher = PasswordHasher(BasicSalt(cfg.password.salt))
        password_hash = hasher.hash('admin')
        query =  AdminModel.insert().values(
            name='admin',
            hashed_password=password_hash,
        )

        return await conn.execute(query)

if __name__ == '__main__':
    asyncio.run(main())

