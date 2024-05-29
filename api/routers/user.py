from typing import Tuple

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncEngine

from api.config import cfg
from api.depends.admin import get_id
from core.db import engine
from exceptions import AdminIsNotLoginError
from facades.user import User
from helpers.authentication import BasicSalt, PasswordHasher
from schemas.user import CreateuserSchema

router = APIRouter(prefix="/admin", tags=["User Management"])


salt = BasicSalt(cfg.password.salt)
hash_ = PasswordHasher(salt)

@router.post("/create/user")
async def create(
        data: CreateuserSchema,
        admin_conn: Tuple[int, AsyncConnection] = Depends(get_id),
) -> int:
    """
    Route For Create user
    :param data:
    :param admin_conn:
    :return:
    """
    admin_id, conn = admin_conn
    try:
        return await User(conn).create(data, hash_, admin_id)
    except AdminIsNotLoginError:
        raise HTTPException(401, detail="Please Login Again")


@router.post("/register/user")
async def registration(
        data: CreateuserSchema,
) -> int:
    """
    Function for registration route
    :param data:
    :return:
    """

    async with engine.begin() as conn:
        t = User(conn)

        return await t.create(data, hash_, is_registration=True)

@router.get("/listing/user")
async def listing(
        admin_conn: Tuple[int, AsyncConnection] = Depends(get_id),
):
    """
    route for listing user
    :param admin_conn:
    :return:
    """
    admin_id, conn = admin_conn
    try:
        return await User(conn).listing(admin_id)
    except AdminIsNotLoginError:
        raise HTTPException(401, detail="Please Login Again")

@router.get("/update-password/user")
async def update_password(
        user_id: int,
        password: str,
        admin_conn: Tuple[int, AsyncConnection] = Depends(get_id),
) -> int:
    """
    Route For Create user
    :param data:
    :param admin_conn:
    :return:
    """
    admin_id, conn = admin_conn
    try:
        return await User(conn).update_password(user_id,password, hash_, admin_id)
    except AdminIsNotLoginError:
        raise HTTPException(401, detail="Please Login Again")
