from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.databases.postgres import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)
router = APIRouter(tags=["Users"])


@router.get("/")
def home():
    return {
        "message": "Welcome to the Enterprise AI Knowledge Assistant API!"
    }


@router.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@router.get(
    "/users/{user_id}",
    response_model=UserResponse
)
def read_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_by_id(db, user_id)

@router.get("/search")
def search_items(q: str):
    return {
        "query": q
    }


@router.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)

@router.get(
    "/users",
    response_model=list[UserResponse]
)
def read_all_users(
    db: Session = Depends(get_db)
):
    return get_all_users(db)
@router.put(
    "/users/{user_id}",
    response_model=UserResponse
)
def update_existing_user(
    user_id: int,
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return update_user(db, user_id, user)

@router.delete("/users/{user_id}")
def delete_existing_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return delete_user(db, user_id)