import attrs
from sqlalchemy.ext.asyncio import AsyncConnection

from api.config import cfg
from crud.admin import AdminRead
from exceptions import AdminPasswordError
from helpers.authentication import PasswordHasher
from helpers.token_maker import TokenMaker
from schemas.admin import AdminLoginSchema


@attrs.define
class Admin:
    """
    Class for facades admin login
    """
    conn: AsyncConnection

    async def login(self, data: AdminLoginSchema, hasher: PasswordHasher):
        """
        Method for login
        :param data:
        :param hasher:
        :return:
        """
        data = data.__dict__
        try:
            check_login = await AdminRead(self.conn).login(data, hasher)
            token = TokenMaker()

            return token.return_token(
                cfg.password.token_key, check_login
            )
        except AdminPasswordError as e:
            raise AdminPasswordError

    async def read_by_name(self, name: str):
        """
        Method for read by name
        :param name:
        :return:
        """
        return await AdminRead(self.conn).read_by_name(name)

    async def logout(self, admin_id: int):
        """
        Method for logout admin
        :param admin_id:
        :return:
        """
        return await AdminRead(self.conn).logout(admin_id)
