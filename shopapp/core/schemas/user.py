from typing import Optional
from fastapi_users import schemas

from pydantic import BaseModel

from core.types.user_id import UserIdType


class UserBase(BaseModel):
    first_name: str
    last_name: str


class UserRead(UserBase, schemas.BaseUser[UserIdType]):
    pass


class UserCreate(UserBase, schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    first_name: Optional[str]
    last_name: Optional[str]
