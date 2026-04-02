from fastapi import FastAPI

app = FastAPI(
    title="Finanace Dashboard Backend",
    description="Backend Api for finance data and role based access control.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "success": True,
        "message": "Finance dashboard backend is running."
    }
