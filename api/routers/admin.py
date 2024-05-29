from typing import Tuple

from fastapi import APIRouter
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncConnection

from api.config import cfg
from api.depends.admin import get_id
from core.db import engine
from exceptions import AdminPasswordError
from facades.admin import Admin
from helpers.authentication import BasicSalt, PasswordHasher
from schemas.admin import AdminLoginSchema

router = APIRouter(prefix='/admin', tags=["Admin"])

@router.post("/login")
async def login(data: OAuth2PasswordRequestForm = Depends()):
    """
    Route For Admin Login
    :param data:
    :return:
    """
    salt = BasicSalt(cfg.password.salt)
    hash_ = PasswordHasher(salt)
    async with engine.begin() as conn:
        try:
            return await Admin(
                conn
            ).login(
                AdminLoginSchema(
                    name=data.username,
                    password=data.password
                ), hash_
            )
        except AdminPasswordError as e:
            raise HTTPException(401, detail="Login Failed")

@router.get("/logout")
async def listing(
        admin_conn: Tuple[int, AsyncConnection] = Depends(get_id),
):
    """
    route for listing user
    :param admin_conn:
    :return:
    """
    admin_id, conn = admin_conn

    return await Admin(conn).logout(admin_id)