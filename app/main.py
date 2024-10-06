import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.error.handler import BaseCustomException, base_custom_exception_handler

app = FastAPI(title="Mozy")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(BaseCustomException, base_custom_exception_handler)



if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
