from fastapi import  APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.schemas.auth import LoginRequest
from app.schemas.user import UserResponse
from app.services.auth_service import login_user
from app.models.user import User

router =APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    result = login_user(db, payload.email,payload.password)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email, password, or inactive account"
        )
    
    return{
        "success": True,
        "message": "Login Successful",
        "data":{
            "access_token": result["access_toker"],
            "token_type": result["token_type"],
            "user": UserResponse.model_validate(result["user"])
        }
    }

@router.get("/me",response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user