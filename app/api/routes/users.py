from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api.deps import get_db, require_roles
from app.models.user  import User
from app.models.enums import UserRole
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user_service import create_user, get_all_user, update_user

router = APIRouter(prefix="/api/users",tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_new_user(
    payload: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.ADMIN))
):
    return create_user(db, payload)

@router.get("/",response_model=list[UserResponse])
def list_users(
    role:Optional[UserRole]=Query(None),
    is_active: Optional[bool]= Query(None),
    db: Session = Depends(get_db),
    current_user: User=Depends(require_roles(UserRole.ADMIN))
):
    return get_all_user(db,role=role,is_active=is_active)

@router.patch("/{user_id}", response_model=UserResponse)
def update_existing_user(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(UserRole.ADMIN))
):
    return update_user(db, user_id, payload)