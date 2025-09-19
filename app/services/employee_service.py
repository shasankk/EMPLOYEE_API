from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeOut
from fastapi import HTTPException, status

def create_employee(db: Session, employee_in: EmployeeCreate):
    db_employee = Employee(**employee_in.dict(exclude_unset=True))
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return EmployeeOut.from_orm(db_employee)

def list_employees(db: Session, page: int = 1, page_size: int = 20, search: str = None):
    query = db.query(Employee)
    if search:
        query = query.filter(Employee.emailid.ilike(f"%{search}%"))  # Example search on emailid
    total = query.count()
    items = query.offset((page - 1) * page_size).limit(page_size).all()
    return items, total

def get_employee(db: Session, employee_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return EmployeeOut.from_orm(employee)

def update_employee(db: Session, employee_id: int, employee_in: EmployeeUpdate):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    update_data = employee_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return EmployeeOut.from_orm(db_employee)

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(db_employee)
    db.commit()