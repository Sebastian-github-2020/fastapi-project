from fastapi import APIRouter

index_router = APIRouter()


@index_router.get("/home")
def index():
    return {
        "msg": "index"
    }
