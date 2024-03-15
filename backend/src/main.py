from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers import all_routers

app = FastAPI(title="DevOps game")

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


for router in all_routers:
    app.include_router(router)
