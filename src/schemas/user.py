from schemas.base import BaseSchema


class CreateUserSchema(BaseSchema):
    login: str
    password: str


class GetUserSchema(CreateUserSchema):
    id: int
