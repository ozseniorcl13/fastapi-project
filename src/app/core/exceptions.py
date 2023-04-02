from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
from app.core.logger import logger
import json

class Exceptions():

    def __init__(self, api: FastAPI) -> None:

        @api.exception_handler(StarletteHTTPException)
        async def http_exception_handler(request, exc):
            logger.error(str(exc.detail))
            return JSONResponse(
                content={'detail': str(exc.detail)},
                status_code=exc.status_code)
        
        @api.exception_handler(RequestValidationError)
        async def validation_exception_handler(request, exc):
            logger.error(str(exc))
            return JSONResponse(
                content={'detail': str(exc)},
                status_code=status.HTTP_400_BAD_REQUEST)