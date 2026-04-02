from fastapi import FastAPI
from app.api.routes import health
app = FastAPI(
    title="Finanace Dashboard Backend",
    description="Backend Api for finance data and role based access control.",
    version="1.0.0"
)
app.include_router(health.router)

@app.get("/")
def root():
    return {
        "success": True,
        "message": "Finance dashboard backend is running."
    }
