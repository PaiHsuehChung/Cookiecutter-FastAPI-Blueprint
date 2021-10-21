import sys
from loguru import logger
from fastapi import FastAPI

from containers.application import Application
from app.router import users, health
from config.settings import get_settings


def initialize():
    settings = get_settings()
    container = Application()
    container.config.from_pydantic(settings)
    container.core.init_resources()
    container.wire(modules=[sys.modules[__name__], users, health])
    return container


def create_app(init_container) -> FastAPI:
    app = FastAPI(root_poath="/api/v1")
    app.include_router(users.router, prefix="/users")
    app.include_router(health.router, prefix="/status")

    app.container = init_container

    return app


app = create_app(initialize())


@app.on_event("startup")
async def startup_event():
    logger.debug("Application startup")
    app.container.services.init_resources()


@app.on_event("shutdown")
async def shutdown_event():
    logger.debug("Application shutdown")
    app.container.services.shutdown_resources()


@app.get("/", include_in_schema=False)
def index():
    project_name = "{{ cookiecutter.project_name }}"
    applictaion_version = "{{ cookiecutter.application_version }}"
    logger.debug(f"Project: {project_name} - Version: {applictaion_version}")
    return {"project": project_name, "version": applictaion_version}
