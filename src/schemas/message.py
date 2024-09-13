from schemas.base import BaseSchema


class CreateMessageSchema(BaseSchema):
    text: str
    author_id: int


class GetMessageSchema(CreateMessageSchema):
    id: int
