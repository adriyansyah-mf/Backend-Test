from pydantic import BaseModel, Field

class AdminLoginSchema(BaseModel):
    """
    Class For Schema Admin Login
    """
    name: str = Field(...)
    password: str = Field(...)
