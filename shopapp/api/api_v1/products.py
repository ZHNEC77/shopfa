from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.schemas.products import ProductRead, ProductCreate
from crud import products as products_crud

router = APIRouter(
    prefix=settings.api.v1.products,
    tags=["Products"],
)


@router.get("", response_model=list[ProductRead])
async def get_products(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    users = await products_crud.get_all_products(session=session)
    return users


@router.post("", response_model=ProductRead)
async def create_product(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    product_create: ProductCreate,
):
    product = await products_crud.create_product(
        session=session,
        product_create=product_create,
    )
    return product
