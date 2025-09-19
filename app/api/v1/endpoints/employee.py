from fastapi import APIRouter, status, Query, Depends
from sqlalchemy.orm import Session
from typing import Optional
from app.core.database import get_db
from app.services import employee_service
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeOut
from app.utils.response import success_response, error_response
from app.core.security import get_current_user

router = APIRouter(
    prefix="/employees",
    tags=["employees"],
    dependencies=[Depends(get_current_user)]  # JWT dependency for all endpoints
)

@router.post("", response_model=None)
def create_employee(payload: EmployeeCreate, db: Session = Depends(get_db)):
    try:
        emp = employee_service.create_employee(db, payload)
        return success_response(
            "Employee created",
            emp.dict(by_alias=True),
            status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        return error_response(
            str(e.detail if hasattr(e, "detail") else str(e)),
            status_code=getattr(e, "status_code", 400)
        )

@router.get("", response_model=None)
def list_employees(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    try:
        items, total = employee_service.list_employees(db, page=page, page_size=page_size, search=search)
        data = [EmployeeOut.from_orm(i).dict(by_alias=True) for i in items]
        pagination = {
            "page": page,
            "pageSize": page_size,
            "totalRecords": total,
            "totalPages": (total + page_size - 1) // page_size
        }
        return success_response("List of employees", data=data, pagination=pagination)
    except Exception as e:
        return error_response(str(e), status_code=getattr(e, "status_code", 400))

@router.get("/{employee_id}", response_model=None)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    try:
        emp = employee_service.get_employee(db, employee_id)
        return success_response("Employee retrieved successfully", emp.dict(by_alias=True))
    except Exception as e:
        return error_response(str(e), status_code=getattr(e, "status_code", 400))

@router.put("/{employee_id}", response_model=None)
def update_employee(employee_id: int, payload: EmployeeUpdate, db: Session = Depends(get_db)):
    try:
        emp = employee_service.update_employee(db, employee_id, payload)
        return success_response("Employee updated", emp.dict(by_alias=True))
    except Exception as e:
        return error_response(str(e), status_code=getattr(e, "status_code", 400))

@router.delete("/{employee_id}", response_model=None)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    try:
        employee_service.delete_employee(db, employee_id)
        return success_response("Employee deleted", data=None, status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return error_response(str(e), status_code=getattr(e, "status_code", 400))