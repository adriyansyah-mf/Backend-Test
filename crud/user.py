from typing import List

import attrs
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection

from api.config import cfg
from helpers.token_maker import TokenMaker
from models import UserModel
from schemas.user import CreateuserSchema, ListingUserSchema


@attrs.define
class UserCrud:
    """
    class User Crud
    """
    conn: AsyncConnection

    async def create(self, data: CreateuserSchema) -> int:
        """
        Method Create user
        :param data:
        :return:
        """

        val = data.dict()
        query = UserModel.insert().values(
            **val
        )

        return (await self.conn.execute(query)).inserted_primary_key[0]

    async def listing(self) -> List[ListingUserSchema]:
        """
        listing method
        :return:
        """
        query = (
            select(
                UserModel.c.id,
                UserModel.c.name
            ).select_from(UserModel)
        )
        data = []
        rows = (await self.conn.execute(query)).fetchall()
        for row in rows:
            data.append(
                ListingUserSchema(
                    name=row.name,
                    id=row.id
                )
            )

        return data

    async def update_password(self, user_id: int, password: str) -> bool:
        """
        Method for change user password
        :return:
        """
        query = (
            UserModel.update()
            .values(
                hashed_password=password).where(
            UserModel.c.id == user_id
        )
        )

        await self.conn.execute(query)
        return True


    
