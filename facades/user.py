from typing import Optional

import attrs
from sqlalchemy.ext.asyncio import AsyncConnection
from crud.admin import AdminRead
from crud.user import UserCrud
from exceptions import AdminIsNotLoginError
from helpers.authentication import PasswordHasher
from schemas.user import CreateuserSchema


@attrs.define
class User:
    """
    Facades for handle user
    """
    conn: AsyncConnection

    async def create(self, data: CreateuserSchema, hasher: PasswordHasher, admin_id: Optional[int] =  None, is_registration: Optional[bool]= None):
        """
        Method for handle create user
        :param data:
        :return:
        """
        if is_registration is not True:
            if AdminRead(self.conn).check_login(admin_id) is False and admin_id is not None:
                raise AdminIsNotLoginError

        data.hashed_password = hasher.hash(data.hashed_password)
        return await UserCrud(self.conn).create(
            data
        )

    async def listing(self, admin_id: int):
        """
        Method for listing user
        :return:
        """
        if await AdminRead(self.conn).check_login(admin_id) is False:
            raise AdminIsNotLoginError

        return await UserCrud(self.conn).listing()

    async def update_password(self, user_id: int,password: str, hasher: PasswordHasher, admin_id: int):
        """
        Method for handle create user
        :param data:
        :return:
        """
        if AdminRead(self.conn).check_login(admin_id) is False:
            raise AdminIsNotLoginError

        password = hasher.hash(password)
        return await UserCrud(self.conn).update_password(
            user_id, password
        )