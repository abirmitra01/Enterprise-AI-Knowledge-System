from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.databases.postgres import Base


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    filename: Mapped[str]

    filetype: Mapped[str]

    filepath: Mapped[str]
    processed_path: Mapped[str]

    uploaded_by: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )