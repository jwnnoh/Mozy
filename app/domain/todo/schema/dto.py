from typing import List
from pydantic import Field, BaseModel


class ToDo(BaseModel):
    task: str = Field(description="The list of tasks to be done.")
    origin: str = Field(description="The origin of the task.")


class ToDos(BaseModel):
    tasks: List[ToDo]


class Memo(BaseModel):
    content: str
