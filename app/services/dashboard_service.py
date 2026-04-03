from sqlalchemy.orm import Session
from sqlalchemy import func, case, extract

from app.models.record import FinancialRecord
from app.models.enums import RecordType


def get_summary(db: Session):
    total_income = db.query(
        func.coalesce(func.sum(FinancialRecord.amount), 0)
    ).filter(
        FinancialRecord.type == RecordType.INCOME,
        FinancialRecord.is_deleted == False
    ).scalar()

    total_expense = db.query(
        func.coalesce(func.sum(FinancialRecord.amount), 0)
    ).filter(
        FinancialRecord.type == RecordType.EXPENSE,
        FinancialRecord.is_deleted == False
    ).scalar()

    record_count = db.query(FinancialRecord).filter(
        FinancialRecord.is_deleted == False
    ).count()

    return {
        "total_income": float(total_income),
        "total_expense": float(total_expense),
        "net_balance": float(total_income) - float(total_expense),
        "record_count": record_count
    }


def get_category_breakdown(db: Session):
    results = db.query(
        FinancialRecord.category,
        func.sum(FinancialRecord.amount).label("total")
    ).filter(
        FinancialRecord.is_deleted == False
    ).group_by(FinancialRecord.category).all()

    return [
        {
            "category": row.category,
            "total": float(row.total)
        }
        for row in results
    ]


def get_monthly_trends(db: Session):
    results = db.query(
        extract("year", FinancialRecord.date).label("year"),
        extract("month", FinancialRecord.date).label("month"),
        func.sum(
            case(
                (FinancialRecord.type == RecordType.INCOME, FinancialRecord.amount),
                else_=0
            )
        ).label("income"),
        func.sum(
            case(
                (FinancialRecord.type == RecordType.EXPENSE, FinancialRecord.amount),
                else_=0
            )
        ).label("expense")
    ).filter(
        FinancialRecord.is_deleted == False
    ).group_by(
        extract("year", FinancialRecord.date),
        extract("month", FinancialRecord.date)
    ).order_by(
        extract("year", FinancialRecord.date),
        extract("month", FinancialRecord.date)
    ).all()

    return [
        {
            "year": int(row.year),
            "month": int(row.month),
            "income": float(row.income),
            "expense": float(row.expense)
        }
        for row in results
    ]


def get_recent_activity(db: Session, limit: int = 5):
    results = db.query(FinancialRecord).filter(
        FinancialRecord.is_deleted == False
    ).order_by(
        FinancialRecord.created_at.desc()
    ).limit(limit).all()

    return results