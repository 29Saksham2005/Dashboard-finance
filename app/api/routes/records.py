from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api.deps import get_db, require_roles, get_current_user
from app.models.user import User
from app.models.enums import UserRole, RecordType
from app.schemas.record import RecordCreate, RecordUpdate, RecordResponse
from app.schemas.record_query import RecordFilterParams
from app.services.record_service import (
    create_record,
    get_records,
    get_record_by_id,
    update_record,
    soft_delete_record
)

router = APIRouter(prefix="/api/records", tags=["Records"])


@router.post("/", response_model=RecordResponse)
def create_new_record(
    payload: RecordCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.ADMIN))
):
    return create_record(db, payload, current_user.id)


@router.get("/", response_model=list[RecordResponse])
def list_records(
    type: Optional[RecordType] = Query(None),
    category: Optional[str] = Query(None),
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.ADMIN, UserRole.ANALYST))
):
    filters = RecordFilterParams(
        type=type,
        category=category,
        start_date=start_date,
        end_date=end_date,
        page=page,
        limit=limit
    )

    return get_records(db, filters)


@router.get("/{record_id}", response_model=RecordResponse)
def get_single_record(
    record_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.ADMIN, UserRole.ANALYST))
):
    return get_record_by_id(db, record_id)


@router.patch("/{record_id}", response_model=RecordResponse)
def update_existing_record(
    record_id: int,
    payload: RecordUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.ADMIN))
):
    return update_record(db, record_id, payload)


@router.delete("/{record_id}")
def delete_record(
    record_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.ADMIN))
):
    return soft_delete_record(db, record_id)