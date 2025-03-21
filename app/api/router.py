from fastapi import APIRouter
from app.api.console import *
from app.config import configs as p

router = APIRouter()

router.include_router(base_router, tags=['Base'])
router.include_router(template_router, tags=['Template'], prefix="/api/template")