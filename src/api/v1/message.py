from fastapi import APIRouter, status, Depends

from schemas.message import CreateMessageSchema, GetMessageSchema
from services.message import MessageService

router = APIRouter(prefix="/messages")


@router.post(
    "/", tags=["Messages"], status_code=status.HTTP_201_CREATED, response_model=None
)
async def create_message(
    message: CreateMessageSchema, message_service: MessageService = Depends()
) -> None:
    await message_service.create_message(message=message)


@router.get(
    "/{id}",
    tags=["Messages"],
    status_code=status.HTTP_200_OK,
    response_model=GetMessageSchema,
)
async def get_message_by_id(
    id: int, message_service: MessageService = Depends()
) -> GetMessageSchema:
    return await message_service.get_message_by_id(id=id)
