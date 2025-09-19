from sqlalchemy.orm import Session
from ..repositories import user_repository
from ..core.security import hash_password, verify_password, create_access_token
from ..schemas.user import UserCreate, UserOut
from ..schemas.token import Token
from ..core.config import settings
from datetime import timedelta
from fastapi import HTTPException, status

# def register_user(db: Session, user_in: UserCreate) -> UserOut:
#     existing = user_repository.get_user_by_email(db, user_in.email)
#     if existing:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
#     hashed = hash_password(user_in.password)
#     user = user_repository.create_user(db, email=user_in.email, hashed_password=hashed)
#     return UserOut.from_orm(user)
def register_user(db: Session, user_in: UserCreate) -> UserOut:
    existing = user_repository.get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    hashed = hash_password(user_in.password)
    user = user_repository.create_user(db, email=user_in.email, hashed_password=hashed)
    return UserOut.from_orm(user)

# def authenticate_user(db: Session, email: str, password: str) -> Token:
#     user = user_repository.get_user_by_email(db, email)
#     if not user or not verify_password(password, user.hashed_password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials")
#     access = create_access_token(subject=user.email, expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
#     return Token(access_token=access, token_type="bearer")
def authenticate_user(db: Session, email: str, password: str) -> Token:
    user = user_repository.get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials")
    access = create_access_token(subject=user.email, expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    return Token(access_token=access, token_type="bearer")