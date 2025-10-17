from datetime import datetime
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import mapped_column, Mapped
from typing import Annotated

from src.database.base_class import Base

int_pk = Annotated[int, mapped_column(primary_key=True)]


class MealTable(Base):
    __tablename__ = 'meals'

    id: Mapped[int_pk]
    meal_name: Mapped[str]
    description: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc',now())"))


