from sqlalchemy.orm import Session
from app.models.employee import Employee
from sqlalchemy import or_
from datetime import datetime

def create_employee(db: Session, employee_data: dict):
    db_employee = Employee(**employee_data, added_date=datetime.utcnow())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()

def get_employee_by_email(db: Session, email: str):
    return db.query(Employee).filter(Employee.emailid == email).first()

def update_employee(db: Session, employee: Employee, changes: dict):
    for key, value in changes.items():
        setattr(employee, key, value)
    db.commit()
    db.refresh(employee)
    return employee

def delete_employee(db: Session, employee: Employee):
    db.delete(employee)
    db.commit()

def list_employees(db: Session, skip: int = 0, limit: int = 20, search: str = None):
    query = db.query(Employee)
    if search:
        search = f"%{search}%"
        query = query.filter(
            or_(
                Employee.first_name.ilike(search),
                Employee.last_name.ilike(search),
                Employee.emailid.ilike(search),
                Employee.department.ilike(search)
            )
        )
    total = query.count()
    items = query.offset(skip).limit(limit).all()
    return items, total