import time
import asyncio
from typing import Callable
from fastapi import FastAPI, Request
from loguru import logger
from starlette_context import context
from settings import settings, Settings
from model.mongodb.collection import Log
import model
from app import error_handler


def init_app(app: FastAPI, app_settings: Settings) -> None:
    """Declare your built-in Functional Middleware"""

    @app.on_event("startup")
    async def startup():
        """run before the application starts"""
        await model.init_app(app, app_settings)
        error_handler.init_app(app)

    @app.on_event("shutdown")
    async def shutdown():
        """run when the application is shutting down"""

    @app.middleware("http")
    async def slow_api_tracker(
            request: Request,
            call_next: Callable):
        """slow api tracker middleware"""
        
        process_time = time.time()
        response = await call_next(request)
        process_time = time.time() - process_time
        response.headers["X-Process-Time"] = str(process_time)

        if process_time >= settings.slow_api_time:
            # Get body in the ContextMiddleware
            request_body = context.get('body')
            log_str: str = (
                f"\n!!! SLOW API DETECTED !!!\n"
                f"time: {process_time}\n"
                f"url: {request.url.path}\n"
                f"ip: {request.client.host}\n")
            log_str += f"body: {str(request_body)}\n"
            logger.error(log_str)

        return response

    if app_settings.mongodb_api_log:
        @app.middleware('http')
        async def mongodb_api_logger(
                request: Request,
                call_next: Callable):
            """
            Mongodb API Logger Middleware
            # How much fast using 'gather'?
            """
            response = await call_next(request)
            await Log().insert_one_raw_dict({
                "ipv4": request.client.host,
                "url": request.url.path,
                'method': request.method,
                'body': (context.get('body') or b'').decode(),
                'status_code': response.status_code,
            })
            return response
