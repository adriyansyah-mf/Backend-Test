from sqlalchemy import Table, Column, BigInteger, Unicode, DateTime, ForeignKey, Text, Boolean
from core.db import meta

AdminModel = Table(
    'admin', meta,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('name', Unicode(100), nullable=False, unique=True),
    Column('hashed_password', Unicode(250), nullable=False),
    Column('is_login', Boolean, default=False)
)