from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin


class Message(BaseModel, IDMixin, CreatedAtMixin):
    __tablename__ = "messages"

    text: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False
    )
