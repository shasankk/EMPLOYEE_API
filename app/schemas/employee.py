from typing import Optional
from .user import CamelModel  # Assuming CamelModel handles camelCase conversion

class EmployeeBase(CamelModel):
    first_name: str
    last_name: Optional[str] = None
    emailid: str
    department: Optional[str] = None
    salary: Optional[float] = None
    status_id: Optional[int] = 1

    class Config:
        # Ensure camelCase is used for JSON serialization
        alias_generator = lambda x: x[0].lower() + x[1:] if x else x
        allow_population_by_field_name = True

class EmployeeCreate(EmployeeBase):
    # Explicitly mark required fields to avoid duplication or misinterpretation
    first_name: str
    emailid: str
    # last_name, department, salary, status_id remain optional as inherited

class EmployeeUpdate(CamelModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    emailid: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None
    status_id: Optional[int] = None

    class Config:
        alias_generator = lambda x: x[0].lower() + x[1:] if x else x
        allow_population_by_field_name = True

class EmployeeOut(EmployeeBase):
    id: int
    added_date: Optional[str] = None

    class Config:
        alias_generator = lambda x: x[0].lower() + x[1:] if x else x
        allow_population_by_field_name = True
