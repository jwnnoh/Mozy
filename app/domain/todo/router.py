from fastapi import APIRouter

from app.domain.todo.core import execute
from app.domain.todo.schema.dto import ToDos, Memo

router = APIRouter(prefix="/api/todo", tags=["todo"])


@router.post("", description="텍스트 기반 TODO 생성 API")
def create_todo(memo: Memo) -> ToDos:
    return execute(memo)
