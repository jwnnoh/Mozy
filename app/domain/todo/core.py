from langchain_core.messages import HumanMessage

from app.config.model import todo_model
from app.domain.todo.exception import ToDoCreateFailException
from app.domain.todo.schema.dto import ToDos, Memo
from app.domain.todo.template import todo_prompt

structured_model = todo_model.with_structured_output(ToDos)
chain = todo_prompt | structured_model


def create_todo(memo: str) -> ToDos:
    response = chain.invoke(
        {
            "content": HumanMessage(content=memo),
        },
    )
    return response


def execute(memo: Memo):
    try:
        response = create_todo(memo.content)
    except Exception:
        raise ToDoCreateFailException

    return response
