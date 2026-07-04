import os
import shutil
import uuid

from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session

from app.models.document import Document
from app.services.processing_service import process_document
from app.models.document import Document
from app.vectorstore.chroma_db import collection

UPLOAD_DIR = "uploads"


def save_document(
    db: Session,
    file: UploadFile,
    user_id: int
):

    allowed_extensions = {
        "pdf",
        "docx",
        "pptx",
        "txt"
    }

    extension = file.filename.split(".")[-1].lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type"
        )

    folder = os.path.join(
        UPLOAD_DIR,
        extension
    )

    os.makedirs(folder, exist_ok=True)

    # Create unique filename
    unique_name = f"{uuid.uuid4()}_{file.filename}"

    filepath = os.path.join(
        folder,
        unique_name
    )

    # Save uploaded file
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process document
    processed_file = process_document(filepath)

    # Save metadata
    document = Document(
        filename=file.filename,
        filetype=extension,
        filepath=filepath,
        processed_path=processed_file,
        uploaded_by=user_id
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    Document(
    filename=file.filename,
    filetype=extension,
    filepath=filepath,
    processed_path=processed_file,
    uploaded_by=user_id
    )

    return document

def get_user_documents(
    db: Session,
    user_id: int
):

    return (

        db.query(Document)

        .filter(

            Document.uploaded_by == user_id

        )

        .order_by(

            Document.id.desc()

        )

        .all()

    )

def delete_document(db: Session, document_id: int, user_id: int):

    document = db.query(Document).filter(
        Document.id == document_id,
        Document.uploaded_by == user_id
    ).first()

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    if os.path.exists(document.filepath):
        os.remove(document.filepath)

    if os.path.exists(document.processed_path):
        os.remove(document.processed_path)

    try:

        results = collection.get()

        ids_to_delete = []

        for vector_id in results["ids"]:

            if vector_id.startswith(document.filename + "_"):

                ids_to_delete.append(vector_id)

        if ids_to_delete:

            collection.delete(ids=ids_to_delete)

            print(f"Deleted {len(ids_to_delete)} vector chunks.")

    except Exception as e:

        print("Chroma delete error:", e)

    db.delete(document)
    db.commit()

    return {
        "message": "Document deleted successfully"
    }
