from fastapi import FastAPI
from app.api.routes import health
from app.core.database import Base, engine

#Import models so SQLAlchemy registers them
from app.models import user, FinancialRecord

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Finanace Dashboard Backend",
    description="Backend Api for finance data and role based access control.",
    version="1.0.0"
)
app.include_router(health.router)

@app.get("/",tags=["Root"])
def root():
    return {
        "success": True,
        "message": "Finance dashboard backend is running."
    }
