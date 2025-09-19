# app/schemas/token.py
from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: str

    class Config:
        from_attributes = True # allow creation from ORM objects
