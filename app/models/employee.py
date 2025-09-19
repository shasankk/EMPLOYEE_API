# app/models/employee.py
from sqlalchemy import Column, Integer, String, Numeric, DateTime, func
from ..core.database import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    emailid = Column(String, unique=True, index=True, nullable=False)
    department = Column(String, nullable=True)
    salary = Column(Numeric, nullable=True)
    status_id = Column(Integer, default=1)  # 1 = active
    added_date = Column(DateTime(timezone=True), server_default=func.now())