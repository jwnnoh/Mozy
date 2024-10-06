from typing import List
from pydantic import Field, BaseModel


class ToDos(BaseModel):
    tasks: List[str] = Field(description="The list of tasks to be done.")


class Memo(BaseModel):
    content: str
