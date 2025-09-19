from fastapi import FastAPI, Depends, HTTPException, status
from .core.logger import logger
from .core.database import engine, Base, get_db
from .core.middleware import request_logging_middleware
from .api.v1.endpoints import auth as auth_router, employee as emp_router
from fastapi.middleware.cors import CORSMiddleware
from .core.security import get_current_user, oauth2_scheme  # Import oauth2_scheme
from .core.security import oauth2_scheme  # Import instead of redefining

def create_app():
    app = FastAPI(title="Employee API", version="1.0")

    # Remove local oauth2_scheme definition
    # oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

    @app.on_event("startup")
    def on_startup():
        logger.info("Creating database tables (if not exist).")
        try:
            Base.metadata.create_all(bind=engine)
        except Exception as e:
            logger.error(f"Failed to create database tables: {str(e)}")
            raise

    try:
        app.middleware("http")(request_logging_middleware)
    except Exception as e:
        logger.error(f"Failed to apply middleware: {str(e)}")
        raise

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth_router.router, prefix="/api/v1", tags=["auth"])
    app.include_router(emp_router.router, prefix="/api/v1", tags=["employees"])

    return app

app = create_app()