from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api.deps import get_db, require_roles
from app.models.user import User
from app.models.enums import UserRole
from app.schemas.dashboard import SummaryResponse, CategoryBreakdownItem, MonthlyTrendItem
from app.schemas.record import RecordResponse
from app.services.dashboard_service import (
    get_summary,
    get_category_breakdown,
    get_monthly_trends,
    get_recent_activity
)

router = APIRouter(prefix="/api/dashboard", tags=["Dashboard"])


@router.get("/summary", response_model=SummaryResponse)
def dashboard_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.ADMIN, UserRole.ANALYST, UserRole.VIEWER))
):
    return get_summary(db)


@router.get("/category-breakdown", response_model=list[CategoryBreakdownItem])
def dashboard_category_breakdown(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.ADMIN, UserRole.ANALYST, UserRole.VIEWER))
):
    return get_category_breakdown(db)


@router.get("/monthly-trends", response_model=list[MonthlyTrendItem])
def dashboard_monthly_trends(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.ADMIN, UserRole.ANALYST, UserRole.VIEWER))
):
    return get_monthly_trends(db)


@router.get("/recent-activity", response_model=list[RecordResponse])
def dashboard_recent_activity(
    limit: int = Query(5, ge=1, le=20),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.ADMIN, UserRole.ANALYST, UserRole.VIEWER))
):
    return get_recent_activity(db, limit=limit)