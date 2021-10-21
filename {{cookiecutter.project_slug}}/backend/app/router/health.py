import logging
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from containers.application import Application

router = APIRouter()


@router.get("/health", include_in_schema=False)
@inject
async def health_check(
    logger: logging=Depends(Provide[Application.core.logger]),
):
    logger.debug(f"Health Check")
    return {"detail": "health"}
