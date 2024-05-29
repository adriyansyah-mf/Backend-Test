from sqlalchemy import Table, Column, BigInteger, Unicode, DateTime, ForeignKey, Text
from core.db import meta

UserModel = Table(
    'user', meta,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('name', Unicode(100), nullable=False),
    Column('hashed_password', Unicode(250), nullable=False)
)