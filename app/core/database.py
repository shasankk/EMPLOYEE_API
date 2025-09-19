from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")
    finally:
        db.close()