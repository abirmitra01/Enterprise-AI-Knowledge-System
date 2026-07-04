
from app.embeddings.embedding_model import model
from app.vectorstore.chroma_db import collection
from app.utils.chunking import chunk_text


def create_embeddings(text, document_name):

    chunks = chunk_text(text)

    embeddings = model.encode(chunks)

    ids = []

    metadatas = []

    for i, chunk in enumerate(chunks):

        ids.append(f"{document_name}_{i}")

        metadatas.append(
            {
                "filename": document_name,
                "chunk": i
            }
        )

    collection.add(

        ids=ids,

        documents=chunks,

        embeddings=embeddings.tolist(),

        metadatas=metadatas

    )