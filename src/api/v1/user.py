from fastapi import APIRouter, status, Depends

from schemas.user import CreateUserSchema, GetUserSchema
from services.user import UserService

router = APIRouter(prefix="/users")


@router.post(
    "/", tags=["Users"], status_code=status.HTTP_201_CREATED, response_model=None
)
async def create_user(
    user: CreateUserSchema, user_service: UserService = Depends()
) -> None:
    await user_service.create_user(user=user)


@router.get(
    "/{login}",
    tags=["Users"],
    status_code=status.HTTP_200_OK,
    response_model=GetUserSchema,
)
async def get_user_by_login(
    login: str, user_service: UserService = Depends()
) -> GetUserSchema:
    return await user_service.get_user_by_login(login=login)
