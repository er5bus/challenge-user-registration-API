"""
    Create fastapi app
"""
import time

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from src.routers import routers

from src.settings.config import configurations
from src.settings.db import database

from src.utils.exceptions import BaseHTTPException


app = FastAPI(
    title=configurations.app_name,
    version=configurations.app_version,
    description=configurations.app_description,
    redoc_url=configurations.redoc_url,
    docs_url=configurations.docs_url,
    openapi_url=configurations.openapi_url,
)

origins, methods, headers = ["*"], ["*"], ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers
)
app.add_middleware(GZipMiddleware)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.exception_handler(BaseHTTPException)
async def unicorn_exception_handler(request: Request, exc: BaseHTTPException):
    return JSONResponse(status_code=exc.status_code, content=exc.to_dict())


@app.exception_handler(Exception)
async def default_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={ 'errorCode': 500, 'reason': str(exc), 'errorMessage': 'Something bad happens' })


for router in routers:
    app.include_router(router)


import asyncio
import uvloop
loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)
