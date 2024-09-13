from fastapi import HTTPException, status


class ModelEncodeValidationError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


login_already_exist_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="User with this login already exist",
)

user_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User not found",
)

message_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Message not found",
)
