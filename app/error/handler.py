from fastapi.responses import JSONResponse
from fastapi import status
from starlette.requests import Request


class BaseCustomException(Exception):
    def __init__(self, is_success: bool, http_status: status, code: int, message: str):
        self.is_success = is_success
        self.http_status = http_status
        self.code = code
        self.message = message


async def base_custom_exception_handler(
        request: Request, exc: BaseCustomException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.http_status,
        content={
            "isSuccess": exc.is_success,
            "code": exc.code,
            "message": exc.message
        }
    )
