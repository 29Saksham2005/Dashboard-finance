from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional

from app.models.enums import UserRole

class UserBase(BaseModel):
    name:str = Field(..., min_length=2,max_length=100)
    email: EmailStr
    role: UserRole =UserRole.VIEWER
    is_active : bool =True

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    role: Optional[UserRole] =  None
    is_active: Optional[bool] = None

class UserResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    password: str =Field(...,min_length=8,max_length=24)