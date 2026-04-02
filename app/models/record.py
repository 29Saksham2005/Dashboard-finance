from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Enum, Numeric, Boolean,TEXT
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.enums import RecordType

class FinancialRecord(Base):
    __tablename__ ="financial_records"

    id= Column(Integer,primary_key=True,index=True)
    amount = Column(Numeric(12,2),nullable=False)
    type = Column(Enum(RecordType),nullable=False)
    category = Column(String,nullable=False)
    date= Column(Date, nullable=False)
    notes= Column(TEXT,nullable=True)

    created_by =Column(Integer,ForeignKey("users.id"),nullable=False)
    is_deleted =Column(Boolean,default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(),onupdate=func.now())

    creator = relationship("User",back_populates="records")