from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.api.deps import get_db

router = APIRouter(prefix="/test-db", tags=["Test DB"])


@router.get("/")
def test_db_connection(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {
        "success": True,
        "message": "Database connection is working"
    }