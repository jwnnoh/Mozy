from app.error.code import ToDoCreateFail
from app.error.handler import BaseCustomException


class ToDoCreateFailException(BaseCustomException):
    def __init__(self):
        super().__init__(
            is_success=False,
            http_status=ToDoCreateFail.HTTP_STATUS.value,
            code=ToDoCreateFail.CODE.value,
            message=ToDoCreateFail.MESSAGE.value
        )
