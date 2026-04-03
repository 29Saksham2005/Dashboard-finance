from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

from app.models.enums import RecordType


class RecordFilterParams(BaseModel):
    type: Optional[RecordType] = None
    category: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    page: int = Field(1, ge=1)
    limit: int = Field(10, ge=1, le=100)