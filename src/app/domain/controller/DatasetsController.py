from typing import Any, List, Optional, Sequence
from fastapi_router_controller import Controller
from fastapi import APIRouter, Body, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse
from app.domain.model.Experiment import Experiment
from app.core.logger import logger
from zope import component
from app.domain.services.IDatasetsService import IDatasetsService

service: IDatasetsService = component.getUtility(IDatasetsService)
router = APIRouter(prefix='/datasets')
controller = Controller(router,openapi_tag={'name':'Datasets'})

@controller.use()
@controller.resource()
class DatasetsController:

    @router.get("/{namespace}", 
                tags=["Datasets"], 
                summary='Validate datasets',
                response_model=None)
    async def validate(namespace: str):
        logger.info(namespace)
        return service.validate(namespace)