from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin, UpdatedAtMixin


class User(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin):
    __tablename__ = "users"

    login: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

