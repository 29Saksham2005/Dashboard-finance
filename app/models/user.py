from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.enums import UserRole

class User(Base):
    __tablename__ = "users"
    id= Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    email = Column(String,unique=True,nullable=False,index=True)
    password_hash = Column(String,nullable=False)
    role = Column(Enum(UserRole),nullable=False,default=UserRole.VIEWER)
    is_active =Column(Boolean, default=True)
    created_at= Column(DateTime(timezone=True), server_default=func.now())
    updated_at= Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())

    records = relationship("FinancialRecord",back_populates="creator")