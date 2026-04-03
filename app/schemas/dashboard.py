from pydantic import BaseModel
from typing import List

from app.schemas.record import RecordResponse


class SummaryResponse(BaseModel):
    total_income: float
    total_expense: float
    net_balance: float
    record_count: int


class CategoryBreakdownItem(BaseModel):
    category: str
    total: float


class MonthlyTrendItem(BaseModel):
    year: int
    month: int
    income: float
    expense: float