from fastapi import Request
from .logger import logger
import time

# async def request_logging_middleware(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     duration = time.time() - start_time
#     logger.info(
#         f"Request: {request.method} {request.url.path} - Status: {response.status_code} - Duration: {duration:.3f}s"
#     )
#     return response
# app/core/middleware.py
async def request_logging_middleware(request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response