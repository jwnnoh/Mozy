from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

from app.domain.todo.prompt import TODO_PROMPT


todo_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(TODO_PROMPT),
        HumanMessagePromptTemplate.from_template("{content}"),
    ]
)
