from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError

from core.exceptions import user_not_found_exception
from db.models import Message
from db.repository.base import BaseDatabaseRepository
from schemas.message import CreateMessageSchema


class MessageRepository(BaseDatabaseRepository):
    async def create_message(self, message: CreateMessageSchema):
        try:
            query = insert(Message).values(**message.dict())

            await self._session.execute(query)
            await self._session.commit()
        except IntegrityError:
            raise user_not_found_exception

    async def get_message_by_id(self, id: int) -> Message | None:
        query = select(Message).where(Message.id == id)

        result = await self._session.execute(query)
        return result.scalars().first()
