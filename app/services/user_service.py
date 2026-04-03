from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password

def create_user(db: Session, payload: UserCreate):
    existing_user= db.query(User).filter(User.email==payload.email).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email already exists"
        )
    new_user= User(
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(payload.password),
        role=payload.role,
        is_active=payload.is_active
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_all_user(db:Session, role=None,is_active=None):
    query =db.query(User)

    if role:
        query=query.filter(User.role == role)
    
    if is_active is not None:
        query = query.filter(User.is_active == is_active)

    return query.order_by(User.created_at.desc()).all()

def update_user(db:Session,user_id:int,payload:UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            message="User not found"
        )
    
    update_data= payload.model_dump(exclude_unset=True)

    for key,value in update_data.items():
        setattr(user,key,value)

    db.commit()
    db.refresh(user)

    return user
