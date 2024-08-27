from fastapi import APIRouter

from core.config import settings
from api.v1.message import router as message_router
from api.v1.user import router as user_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(router=message_router)
v1_router.include_router(router=user_router)

project_router = APIRouter(prefix=f'{settings().PROJECT_NAME}')