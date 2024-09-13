from fastapi import Depends

from core.exceptions import message_not_found_exception
from db.repository.message import MessageRepository
from schemas.message import CreateMessageSchema, GetMessageSchema
from services.base import BaseService


class MessageService(BaseService):
    def __init__(self, message_repository: MessageRepository = Depends()):
        self._message_repository = message_repository

    async def create_message(self, message: CreateMessageSchema):
        await self._message_repository.create_message(message=message)

    async def get_message_by_id(self, id: int) -> GetMessageSchema:
        message = await self._message_repository.get_message_by_id(id=id)

        if not message:
            raise message_not_found_exception

        return GetMessageSchema.model_validate(message)
