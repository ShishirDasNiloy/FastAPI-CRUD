from routes import roles
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(roles.router, prefix='/roles', tags=["Roles"])