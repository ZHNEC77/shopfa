from typing import Annotated
from fastapi import APIRouter, Depends

from api.api_v1.fastapi_users_router import curent_user, curent_superuser
from core.config import settings
from core.models import User
from core.schemas.user import UserRead


router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Messages"],
)


@router.get("")
def get_user_messages(
    user: Annotated[
        User,
        Depends(curent_user)
    ],
):
    return {
        "messages": ["Welcome", "Your status - User"],
        "user": UserRead.model_validate(user),
    }


@router.get("/supuser")
def get_superuser_messages(
    user: Annotated[
        User,
        Depends(curent_superuser)
    ],
):
    return {
        "messages": ["Welcome", "Your status - Super User"],
        "user": UserRead.model_validate(user),
    }
