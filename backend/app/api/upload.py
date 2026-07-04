from fastapi import APIRouter, UploadFile, File, Depends

from sqlalchemy.orm import Session

from app.databases.postgres import get_db

from app.schemas.document import DocumentResponse

from app.services.upload_service import save_document

from app.core.security import get_current_user

from app.models.user import User

from app.services.upload_service import get_user_documents

from app.core.security import get_current_user

from app.models.user import User
from app.services.upload_service import delete_document

router = APIRouter(

    prefix="/documents",

    tags=["Documents"]

)


@router.post(

    "/upload",

    response_model=DocumentResponse

)

def upload_document(

    file: UploadFile = File(...),

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return save_document(

        db=db,

        file=file,

        user_id=current_user.id

    )

@router.get(
    "/my",
    response_model=list[DocumentResponse]
)
def my_documents(

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return get_user_documents(

        db,

        current_user.id

    )

@router.delete("/{document_id}")
def delete_uploaded_document(

    document_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return delete_document(

        db,

        document_id,

        current_user.id

    )