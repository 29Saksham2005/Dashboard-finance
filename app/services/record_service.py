from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import and_

from app.models.record import FinancialRecord
from app.schemas.record import RecordCreate, RecordUpdate
from app.schemas.record_query import RecordFilterParams


def create_record(db: Session, payload: RecordCreate, user_id: int):
    new_record = FinancialRecord(
        amount=payload.amount,
        type=payload.type,
        category=payload.category,
        date=payload.date,
        notes=payload.notes,
        created_by=user_id
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return new_record


def get_records(db: Session, filters: RecordFilterParams):
    query = db.query(FinancialRecord).filter(FinancialRecord.is_deleted == False)

    if filters.type:
        query = query.filter(FinancialRecord.type == filters.type)

    if filters.category:
        query = query.filter(FinancialRecord.category.ilike(f"%{filters.category}%"))

    if filters.start_date:
        query = query.filter(FinancialRecord.date >= filters.start_date)

    if filters.end_date:
        query = query.filter(FinancialRecord.date <= filters.end_date)

    offset = (filters.page - 1) * filters.limit

    return query.order_by(FinancialRecord.date.desc()).offset(offset).limit(filters.limit).all()


def get_record_by_id(db: Session, record_id: int):
    record = db.query(FinancialRecord).filter(
        and_(
            FinancialRecord.id == record_id,
            FinancialRecord.is_deleted == False
        )
    ).first()

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found"
        )

    return record


def update_record(db: Session, record_id: int, payload: RecordUpdate):
    record = db.query(FinancialRecord).filter(
        and_(
            FinancialRecord.id == record_id,
            FinancialRecord.is_deleted == False
        )
    ).first()

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found"
        )

    update_data = payload.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(record, key, value)

    db.commit()
    db.refresh(record)

    return record


def soft_delete_record(db: Session, record_id: int):
    record = db.query(FinancialRecord).filter(
        and_(
            FinancialRecord.id == record_id,
            FinancialRecord.is_deleted == False
        )
    ).first()

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found"
        )

    record.is_deleted = True
    db.commit()

    return {"message": "Record deleted successfully"}