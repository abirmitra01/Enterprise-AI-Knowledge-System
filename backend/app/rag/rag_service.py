from app.vectorstore.chroma_db import collection
from app.embeddings.embedding_model import model


def build_prompt(question: str):

    embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3,
        include=["documents", "metadatas", "distances"]
    )

    documents = []
    sources = []

    docs = results["documents"][0]
    metas = results["metadatas"][0]
    distances = results["distances"][0]

    for doc, meta, distance in zip(docs, metas, distances):

        if distance < 1.2:

            documents.append(doc)

            filename = (
                meta.get("filename")
                or meta.get("document")
                or "Unknown"
            )

        if filename not in sources:
            sources.append(filename)

    if len(documents) == 0:

        return None, []

    context = "\n\n".join(documents)

    prompt = f"""
You are an Enterprise AI Knowledge Assistant.

Answer ONLY from the context below.

Rules:

• Maximum 60 words.

• Prefer bullet points.

• Never guess.

• Never repeat yourself.

• If answer doesn't exist, say:
'I couldn't find that information in the uploaded documents.'

Context:

{context}

Question:

{question}

Answer:
"""

    return prompt, sources