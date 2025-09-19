from fastapi.responses import JSONResponse
from typing import Any, Dict, List, Optional

def success_response(message: str, data: Any = None, pagination: Dict = None, status_code: int = 200) -> JSONResponse:
    response = {"success": True, "message": message}
    if data is not None:
        response["data"] = data
    if pagination:
        response["pagination"] = pagination
    return JSONResponse(status_code=status_code, content=response)

def error_response(message: str, status_code: int = 400, errors: Optional[List[Dict]] = None) -> JSONResponse:
    response = {"success": False, "message": message}
    if errors:
        response["errors"] = errors
    return JSONResponse(status_code=status_code, content=response)