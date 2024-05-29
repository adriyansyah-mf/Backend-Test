import asyncio
from core.db import meta, engine
from models.admin import AdminModel
from models.user import UserModel

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(meta.create_all, tables=[
            AdminModel,
            UserModel
        ])

    await engine.dispose()

if __name__ == '__main__':
    asyncio.run(main())


