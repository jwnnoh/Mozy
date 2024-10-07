from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

todo_model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1
)
