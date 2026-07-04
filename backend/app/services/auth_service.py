from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import UserRegister
from app.core.security import hash_password
from app.core.security import verify_password
from app.core.security import create_access_token

def register_user(
    db:Session,
    user:UserRegister
):

    db_user=User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hash_password(
            user.password
        )
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(
    db: Session,
    username: str,
    password: str
):
    user = db.query(User).filter(
        User.username == username
    ).first()

    if not user:
        return None

    if not verify_password(
        password,
        user.hashed_password
    ):
        return None

    token = create_access_token(
        {
            "sub": user.username
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "username": user.username,
        "full_name": user.full_name
    }