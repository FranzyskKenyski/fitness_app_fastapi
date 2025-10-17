from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, text
from sqlalchemy.orm import relationship, mapped_column, Mapped
from src.database.base_class import Base
from datetime import datetime
from typing import Optional, Annotated


int_pk = Annotated[int, mapped_column(primary_key=True)]


class UserTable(Base):
    __tablename__ = 'users'

    id: Mapped[int_pk]
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc',now())"))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)

# class UserMealTable(Base):
#     __tablename__ = 'user_meals'
#
#     id: Mapped[int_pk]
#     user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
#     meal_id: Mapped[int] = mapped_column(ForeignKey('meals.id'))
#     meal_taken_at: Mapped[datetime] = mapped_column(default=datetime.now)



