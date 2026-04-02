from pydantic import BaseModel, EmailStr
from app.schemas.user import  UserResponse

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoginResponse(BaseModel):
    success: bool
    message: str
    data: dict