from enum import Enum

from starlette import status


class InternalServerError(Enum):
    HTTP_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
    CODE = 500
    MESSAGE = "서버 오류가 발생했습니다."


class ToDoCreateFail(Enum):
    HTTP_STATUS = status.HTTP_503_SERVICE_UNAVAILABLE
    CODE = 503
    MESSAGE = "투두 생성에 실패했습니다."
