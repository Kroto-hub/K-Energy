from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import CORS_ORIGINS
from app.api.router import api_router
from app.database import engine, Base, SessionLocal
from app.services.schema_patch import (
    ensure_construction_template_result_columns,
    ensure_project_building_template_columns,
)
from app.services.template_library_seed import ensure_builtin_template_library
import app.models  # This will trigger __init__.py and import all models


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    ensure_project_building_template_columns()
    ensure_construction_template_result_columns()
    db = SessionLocal()
    try:
        ensure_builtin_template_library(db)
    finally:
        db.close()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="K-Energy API",
        description="能源站初投资与运行费用计算系统",
        version="0.1.0",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix="/api/v1")

    from fastapi.exceptions import RequestValidationError
    from fastapi.responses import JSONResponse
    from fastapi import Request

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        print(f"Validation Error 422! payload: {exc.body}")
        print(f"Errors: {exc.errors()}")
        return JSONResponse(
            status_code=422,
            content={"detail": exc.errors()},
        )

    return app


app = create_app()
