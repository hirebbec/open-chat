from fastapi import Depends

from db.repository.user import UserRepository
from schemas.user import CreateUserSchema, GetUserSchema
from services.base import BaseService
from utils.auth import hash_password


class UserService(BaseService):
    def __init__(self, user_repository: UserRepository = Depends()):
        self._user_repository = user_repository

    async def create_user(self, user: CreateUserSchema) -> None:
        user.password = hash_password(password=user.password)
        await self._user_repository.create_user(user=user)

    async def get_user_by_login(self, login: str) -> GetUserSchema:
        user = await self._user_repository.get_user_by_login(login=login)

        return GetUserSchema.model_validate(user)
