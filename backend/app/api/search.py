from fastapi import APIRouter

from app.services.search_service import search_documents

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/")
def search(
    query: str
):

    return search_documents(query)