from typing import Any, List, Optional, Sequence
from fastapi_router_controller import Controller
from fastapi import APIRouter, Body, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse
from app.domain.model.Experiment import Experiment
from app.core.logger import logger
from zope import component
from app.domain.services.IExperimentService import IExperimentService

service: IExperimentService = component.getUtility(IExperimentService)
router = APIRouter(prefix='/experiments')
controller = Controller(router,openapi_tag={'name':'Experiments'})

@controller.use()
@controller.resource()
class ExperimentsController:

    @router.get("/{namespace}", 
                tags=["Experiments"], 
                summary='List Experiments from Katib',
                response_model=None)
    async def findAllByNamespace(namespace: str):
        logger.info(namespace)
        return service.findAllByNamespace(namespace)