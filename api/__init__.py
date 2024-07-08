import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from adapters.src.repositories.sql import SessionManager, SQLConnection
from api.src.routers import appointment_router, index_router, product_router

origins = os.environ.get("CORS_ORIGINS", "*").split(",")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    connection: SQLConnection = SQLConnection()
    SessionManager.initialize_session(connection)
    yield
    SessionManager.close_session()


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(index_router)
    return app
