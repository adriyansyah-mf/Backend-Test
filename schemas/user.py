import attrs
from pydantic import BaseModel, Field

class CreateuserSchema(BaseModel):
    """
    Schema for create User
    """
    name: str = Field(...)
    hashed_password: str = Field(...)

@attrs.define(slots=False)
class ListingUserSchema:
    """
    Lisitng User Response Schema
    """
    id: int
    name: str