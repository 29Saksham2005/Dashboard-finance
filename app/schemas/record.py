from datetime import date, datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

from app.models.enums import RecordType

class RecordBase(BaseModel):
    amount: Decimal = Field(..., gt=0)
    type: RecordType
    category: str =Field(..., min_length=2,max_length=100)
    date: date
    notes: Optional[str] = Field(None,max_length=500)

class RecordCreate(RecordBase):
    pass

class RecordUpdate(BaseModel):
    amount: Optional[Decimal]= Field(None, gt=0)
    type: Optional[RecordType]= None
    category: Optional[str]= Field(None,min_length=2,max_length=100)
    date: Optional[date] = None
    notes: Optional[str]= Field(None, max_length=500)

class RecordResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    amount: Decimal
    type: RecordType
    category: str
    date: date
    notes: Optional[str]
    created_by: int
    is_deleted: bool
    created_at: datetime
    updated_at: datetime