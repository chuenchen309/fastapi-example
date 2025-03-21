from fastapi import APIRouter
from app.config import configs as p

router = APIRouter()

@router.get("/", operation_id="read_root_get")
async def read_root():
    return {"name": p.APP_NAME, "verion": p.APP_VERSION, "desc": f"The {p.APP_NAME} is already working."}