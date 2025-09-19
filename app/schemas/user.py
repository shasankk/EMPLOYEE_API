from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

def to_camel(string: str) -> str:
    parts = string.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

class CamelModel(BaseModel):
    model_config = {
        "alias_generator": to_camel,
        "populate_by_name": True,
        "from_attributes": True,
        "arbitrary_types_allowed": True  # Allow datetime objects
    }

class UserCreate(CamelModel):
    email: EmailStr
    password: str

class UserOut(CamelModel):
    id: int
    email: EmailStr
    created_at: Optional[str] = None

    @classmethod
    def from_orm(cls, obj):
        data = obj.__dict__
        if 'created_at' in data and isinstance(data['created_at'], datetime):
            data['created_at'] = data['created_at'].isoformat()  # Convert datetime to ISO string
        return super().from_orm(obj)