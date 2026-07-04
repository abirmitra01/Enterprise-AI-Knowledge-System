from sqlalchemy.orm import Mapped, mapped_column

from app.databases.postgres import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username:Mapped[str]=mapped_column(unique=True,index=True)
    email:Mapped[str]=mapped_column(unique=True,index=True)
    hashed_password:Mapped[str]
    full_name:Mapped[str]
    role:Mapped[str]=mapped_column(default="employee")

