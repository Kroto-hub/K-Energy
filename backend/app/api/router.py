from fastapi import APIRouter

from app.api.projects import router as projects_router

api_router = APIRouter()


@api_router.get("/health")
def health_check():
    return {"status": "ok", "message": "K-Energy API is running"}


api_router.include_router(projects_router)
