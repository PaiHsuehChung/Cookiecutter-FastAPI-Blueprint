# Build-in
import logging
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

# Containers
from containers.application import Application


router = APIRouter()


@router.get("/me", include_in_schema=False)
@inject
async def read_me(
    logger: logging = Depends(Provide[Application.core.logger]),
):
    project_owner = "{{ cookiecutter.full_name }}"
    logger.debug(f"Hello: {project_owner}")
    return {"Hello": project_owner}
