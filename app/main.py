from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.routes import health, auth, users, records, dashboard
from app.core.database import Base, engine
from app.core.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler
)


#Import models so SQLAlchemy registers them
from app.models import User, FinancialRecord

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Finanace Dashboard Backend",
    description="Backend Api for finance data and role based access control.",
    version="1.0.0"
)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(records.router)
app.include_router(dashboard.router)

@app.get("/",tags=["Root"])
def root():
    return {
        "success": True,
        "message": "Finance dashboard backend is running."
    }
