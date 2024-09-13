from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError

from core.exceptions import login_already_exist_exception, user_not_found_exception
from db.models import User
from db.repository.base import BaseDatabaseRepository
from schemas.user import CreateUserSchema


class UserRepository(BaseDatabaseRepository):
    async def create_user(self, user: CreateUserSchema) -> None:
        try:
            query = insert(User).values(**user.dict())

            await self._session.execute(query)
            await self._session.commit()

        except IntegrityError:
            raise login_already_exist_exception

    async def get_user_by_login(self, login: str) -> User | None:
        query = select(User).where(User.login == login)
        result = await self._session.execute(query)

        user = result.scalars().first()

        if not user:
            raise user_not_found_exception

        return user
