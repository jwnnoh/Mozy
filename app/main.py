import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.error.handler import BaseCustomException, base_custom_exception_handler
from app.domain.todo import router as todo_router

app = FastAPI(title="Mozy")

origins = [
    "http://localhost:3000",
    "https://mozy-8xl1g25bf-jejins-projects.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo_router.router)

app.add_exception_handler(BaseCustomException, base_custom_exception_handler)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
