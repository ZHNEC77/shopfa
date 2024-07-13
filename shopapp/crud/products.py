from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Product
from core.schemas.products import ProductCreate


async def get_all_products(
    session: AsyncSession,
) -> Sequence[Product]:
    stmt = select(Product).order_by(Product.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_product(
    session: AsyncSession,
    product_create: ProductCreate,
) -> Product:
    product = Product(**product_create.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product
