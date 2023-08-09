from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from typing import Optional

Base: DeclarativeMeta = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, nullable=False)
    user_id: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[Optional[str]] = mapped_column()
    last_name: Mapped[Optional[str]] = mapped_column()
    city: Mapped[Optional[str]] = mapped_column()
    country: Mapped[Optional[str]] = mapped_column()
    bdate: Mapped[Optional[str]] = mapped_column()
    sex: Mapped[Optional[str]] = mapped_column()
