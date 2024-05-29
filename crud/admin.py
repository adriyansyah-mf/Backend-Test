import asyncio

import attrs
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection

from api.config import cfg
from exceptions import AdminPasswordError
from helpers.authentication import PasswordHasher, BasicSalt
from core.db import engine
from models import AdminModel
from schemas.admin import AdminLoginSchema


@attrs.define
class AdminRead:
    """
    Class For Admin
    """
    conn: AsyncConnection

    async def logout(self, admin_id):
        """
        Method for logout
        :return:
        """
        query = (
            AdminModel.update()
            .values(
                is_login=False
            ).where(
                AdminModel.c.id == admin_id
            )
        )

        return await self.conn.execute(query)

    async def check_login(self, id: int) -> bool:
        """
        Check Login
        :param name:
        :return:
        """
        query = (
            select(
                AdminModel.c.is_login
            ).select_from(
                AdminModel
            ).where(
                AdminModel.c.id == id
            )
        )
        data = (await self.conn.execute(query)).first()

        return data.is_login
    async def login(self, data: dict, hasher: PasswordHasher) -> str:
        """
        Method for login
        :param data:
        :param hasher:
        :return:
        """
        username = data['name']
        password = data['password']
        query = (
            select(
                AdminModel.c.hashed_password,
                AdminModel.c.name
            ).select_from(
                AdminModel
            )
        ).where(
            AdminModel.c.name == username
        )

        result = (await self.conn.execute(query)).first()

        if not hasher.verify(password, result.hashed_password):
            raise AdminPasswordError

        query = (
            AdminModel.update()
            .values(
                is_login=True
            ).where(
                AdminModel.c.name == username
            )
        )

        await self.conn.execute(query)

        return result.name

    async def read_by_name(self, name: str):
        """
        Method for read by name
        :param name:
        :return:
        """
        query = (
            select(
                AdminModel.c.id
            ).select_from(AdminModel)
        ).where(
            AdminModel.c.name == name
        )

        return (await self.conn.execute(query)).first()





async def main():
    salt = BasicSalt(cfg.password.salt)
    hash_ = PasswordHasher(salt)
    async with engine.begin() as conn:

        return await AdminRead(
            conn
        ).login(
            AdminLoginSchema(
                name='admin',
                password='admisn'
            ), hash_
        )



if __name__ == '__main__':
    print(asyncio.run(main()))
