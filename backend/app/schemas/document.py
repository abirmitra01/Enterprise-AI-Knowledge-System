from pydantic import BaseModel


class DocumentResponse(BaseModel):

    id: int
    filename: str
    filetype: str
    filepath: str
    processed_path: str
    uploaded_by: int

    model_config = {
        "from_attributes": True
    }