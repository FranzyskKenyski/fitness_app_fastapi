from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from src.database.base_class import Base
from typing import Optional, Annotated

int_pk = Annotated[int, mapped_column(primary_key=True)]

class ProductTable(Base):
    __tablename__ = 'products'

    id: Mapped[int_pk]
    name: Mapped[str]
    description: Mapped[str]
    calories_per_100g: Mapped[float]
    carbs_per_100g: Mapped[float]
    fats_per_100g: Mapped[float]
    proteins_per_100g: Mapped[float]
