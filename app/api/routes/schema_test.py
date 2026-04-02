from fastapi import APIRouter
from app.schemas.record import RecordCreate, RecordResponse

router =APIRouter(prefix="/schema-test",tags=["Schema Test"])

@router.post("/record",response_model=RecordCreate)
def test_record_schema(payload: RecordCreate):
    return payload