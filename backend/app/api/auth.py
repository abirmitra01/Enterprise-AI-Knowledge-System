from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.databases.postgres import get_db
from app.schemas.auth import UserRegister
from app.services.auth_service import register_user
from fastapi import HTTPException
from app.schemas.auth import UserLogin
from app.services.auth_service import login_user

router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")

def register(

    user:UserRegister,

    db:Session=Depends(get_db)

):

    return register_user(
        db,
        user
    )

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    token = login_user(
        db,
        user.username,
        user.password
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return token