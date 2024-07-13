from sqlalchemy.orm import Mapped

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


class Product(IntIdPkMixin, Base):

    name: Mapped[str]
    discription: Mapped[str]
    price: Mapped[int]
