from app.vectorstore.chroma_db import collection


def search_documents(
    query
):

    results = collection.query(

        query_texts=[query],

        n_results=5
    )

    return results