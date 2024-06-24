from fastapi import APIRouter

index_router = APIRouter()


@index_router.get("/")
async def index() -> dict:
    return {"backend-dental-lab": "0.1"}
