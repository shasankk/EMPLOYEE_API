from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.config import settings
from app.schemas.user import UserCreate, UserOut
from app.services.auth_service import register_user, authenticate_user
from app.utils.response import success_response, error_response
from app.core.logger import logger
from app.schemas.token import Token
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import ValidationError

router = APIRouter(prefix="/auth", tags=["auth"])  # Relative path

@router.post("/register", response_model=None)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    try:
        user = register_user(db, user_in)
        return success_response("User registered", user.dict(by_alias=True))
    except ValidationError as e:
        logger.error(f"Validation error during registration: {str(e)}", exc_info=True)
        return error_response("Validation error: Invalid user data", status_code=422)
    except Exception as e:
        logger.error(f"Registration failed: {str(e)}", exc_info=True)
        error_msg = str(e.detail if hasattr(e, "detail") else "An error occurred during registration")
        return error_response(error_msg, status_code=getattr(e, "status_code", 400))

@router.post("/login", response_model=None)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        token = authenticate_user(db, form_data.username, form_data.password)
        return success_response("Login successful", data=token.dict())
    except Exception as e:
        logger.error(f"Login failed: {str(e)}", exc_info=True)
        return error_response(str(e.detail if hasattr(e, "detail") else "Invalid credentials"), status_code=getattr(e, "status_code", 401))